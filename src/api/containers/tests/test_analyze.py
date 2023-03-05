from infra.storage.structs import Identifier
from infra.data_frames.pipeline import *  # noqa


def test_analyze_container_with_empty_matches_df(csv_analyze_container, matches_csv, mock_repository):
    mock_repository.get_one.return_value = matches_csv

    pipeline = Pipeline.fill_from([
        StripColumnName,
        ClearColumnsFromHyphens,
        CreateWinLoseColumns,
        FilterCompletedGamesColumn,
        CreateWinnerColumn,
        ClearTeams,
    ])

    with csv_analyze_container.repository.override(mock_repository):
        with csv_analyze_container.pipeline.override(pipeline):
            service = csv_analyze_container.service()
            df = service.collect_one(Identifier('test'))

    assert not df.empty
    assert len(df) == 50
    assert df.columns.tolist() == [
        'Date', 'Team1', 'Team2',
        'Map', 'Event', 'Team1 Score',
        'Team2 Score', 'Team1 Won',
        'Team2 Won', 'Winner',
    ]


def test_columns_on_pipeline(csv_analyze_container, matches_csv, mock_repository):
    mock_repository.get_one.return_value = matches_csv

    pipeline = Pipeline.fill_from([
        StripColumnName,
        ClearColumnsFromHyphens,
        CreateWinLoseColumns,
        FilterCompletedGamesColumn,
        CreateWinnerColumn,
        ClearTeams,
        SplitByTeams,
    ])

    with csv_analyze_container.repository.override(mock_repository):
        with csv_analyze_container.pipeline.override(pipeline):
            service = csv_analyze_container.service()
            df = service.collect_one(Identifier('test'))

    assert not df.empty
    assert len(df) == 100
    assert df.columns.tolist() == [
        'Team', 'Score', 'Map',
        'Opponent', 'Opponent Score', 'Date',
        'Event', 'Is Winner',
    ]
