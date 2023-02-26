import re

import pandas as pd

from .base import Handler
from api.services.analyze.utils import make_column, score_is_final


class C:
    Team1 = 'Team1'
    Team2 = 'Team2'
    Team1Score = 'Team1 Score'
    Team2Score = 'Team2 Score'
    Team1Won = 'Team1 Won'
    Team2Won = 'Team2 Won'
    Winner = 'Winner'
    GameCompleted = 'Game Completed'


class ClearColumnsFromHyphens(Handler):
    depends_on = None

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        for column in df.columns:
            df[column].replace({r"\\n": ''}, inplace=True, regex=True)

        return df


class CreateScoreColumns(Handler):
    depends_on = ClearColumnsFromHyphens

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        pattern = re.Pattern(r'\((\d+)\)$')

        df = make_column(df, column_name=C.Team1Score, on_column=C.Team1, pattern=pattern)
        df = make_column(df, column_name=C.Team2Score, on_column=C.Team2, pattern=pattern)

        return df


class CreateWinLoseColumns(Handler):
    depends_on = CreateScoreColumns

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        df[C.Team1Won] = df[C.Team1Score].map(score_is_final)
        df[C.Team2Won] = df[C.Team2Score].map(score_is_final)

        return df


class FilterCompletedGamesColumn(Handler):
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


class ClearTeams(Handler):
    depends_on = CreateScoreColumns

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        pattern = re.Pattern(r'^(.*)\(\d+\)$')

        for column in [C.Team1, C.Team2]:
            df = make_column(df, column_name=column, on_column=column, pattern=pattern)

        return df
