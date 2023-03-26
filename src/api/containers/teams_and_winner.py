from dependency_injector import providers, containers

from infra.storage import DataType, CsvRepository
from infra.storage.factories import *  # noqa
from api.services import DataFramePipelineService
from settings import Settings
from infra.data_frames.pipeline import *  # noqa


class LoadTeamsAndWinnerOnly(containers.DeclarativeContainer):
    config = providers.Configuration(default=Settings().dict())

    repository = providers.Factory(
        CsvRepository,
        context=config.dirs.csv_matches,
        data_type=DataType.MATCHES,
    )

    pipeline = providers.Factory(
        Pipeline.fill_from,
        handlers=[
            CreateWinnerColumn,
            RemoveAllColumnsExcept((C.Team1, C.Team2, C.Winner, C.Map)),
        ],
    )

    df_factory = providers.Factory(
        DataFrameFromCSVFactory,
    )

    service = providers.Factory(
        DataFramePipelineService,
        repository=repository,
        pipeline=pipeline,
        df_factory=df_factory,
    )
