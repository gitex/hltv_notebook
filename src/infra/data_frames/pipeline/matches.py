import re

import pandas as pd

from .base import Handler
from infra.data_frames.pipeline.utils import make_column
from domain.matches.value_objects import Score


class C:
    Team1 = 'Team1'
    Team2 = 'Team2'
    Team1Score = 'Team1 Score'
    Team2Score = 'Team2 Score'
    Team1Won = 'Team1 Won'
    Team2Won = 'Team2 Won'
    Winner = 'Winner'
    GameCompleted = 'Game Completed'
    Map = 'Map'


class StripColumnName(Handler):
    """ Strip whitespace from column names.

    This is a workaround for a bug in the data source.
    """

    depends_on = None

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        df.columns = df.columns.str.strip()

        return df


class ClearColumnsFromHyphens(Handler):
    """ Clear columns from hyphens.

    This is a workaround for a bug in the data source.
    """

    depends_on = None

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        for column in df.columns:
            df[column].replace({r"\\n": ''}, inplace=True, regex=True)

        return df


class CreateScoreColumns(Handler):
    depends_on = ClearColumnsFromHyphens

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        pattern = re.compile(r'\((\d+)\)$')

        for team_column, team_score_column in [(C.Team1, C.Team1Score), (C.Team2, C.Team2Score)]:
            df[team_score_column] = df[team_column].str.extract(pattern, expand=False).astype(int)

        return df


class ClearTeams(Handler):
    depends_on = CreateScoreColumns

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        pattern = re.compile(r'^(.*)\(\d+\)$')

        for column in [C.Team1, C.Team2]:
            df = make_column(df, column_name=column, on_column=column, pattern=pattern)

        return df


class CreateWinLoseColumns(Handler):
    depends_on = ClearTeams

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        columns = (
            (C.Team1Won, C.Team1Score),
            (C.Team2Won, C.Team2Score),
        )

        for new_column, score_column in columns:
            df[new_column] = df[score_column].map(lambda x: Score(int(x)).is_final()).astype(bool)

        return df


class FilterCompletedGamesColumn(Handler):
    """ Filter out games that are completed."""

    depends_on = CreateWinLoseColumns

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        return df[df[C.Team1Won] | df[C.Team2Won]]


class CreateWinnerColumn(Handler):
    depends_on = FilterCompletedGamesColumn

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        winners = []

        for _, row in df.iterrows():
            if row[C.Team1Won]:
                winner = row[C.Team1]
            else:
                winner = row[C.Team2]

            winners.append(winner)

        df[C.Winner] = winners

        return df


class SplitByTeams(Handler):
    """ Split the data frame by teams.


    This is a workaround for a bug in the data source.

    The data source has a single row for each match, but it has two teams.
    This handler splits the data frame into two rows, one for each team.

    The data frame will have the following columns:
        Team - The name of the team
        Score - The score of the team
        Map - The map the match was played on
        Opponent - The name of the opponent team
        Opponent Score - The score of the opponent team
        Date - The date of the match
        Event - The name of the event the match was played in
        Is Winner - Is the team the winner of the match
    """

    depends_on = CreateWinnerColumn

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        initial_columns = (
            ('Team1', 'Team1 Score', 'Winner', 'Map', 'Team2', 'Team2 Score', 'Date', 'Event'),
            ('Team2', 'Team2 Score', 'Winner', 'Map', 'Team1', 'Team1 Score', 'Date', 'Event'),
        )

        new_columns = (
            'Team', 'Score', 'Winner', 'Map', 'Opponent', 'Opponent Score', 'Date', 'Event',
        )

        new_df = pd.DataFrame()

        for part in initial_columns:
            part_df = df[list(part)]
            part_df.rename(columns=dict(zip(part, new_columns)), inplace=True)
            part_df['Is Winner'] = part_df['Team'] == part_df['Winner']
            new_df = pd.concat([new_df, part_df], ignore_index=True)

        del new_df['Winner']
        return new_df


class RemoveAllColumnsExcept(Handler):
    """ Remove all columns except the ones specified. """

    depends_on = None

    def __init__(self, columns: tuple):
        self.columns = columns

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        for column in self.columns:
            if column not in df.columns:
                raise ValueError(f'Column {column} not in data frame.')

        return df.loc[:, self.columns]
