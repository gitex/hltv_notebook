from dependency_injector import providers, containers

from infra.storage import DataType, CsvRepository
from infra.storage.factories import *  # noqa
from api.services import AnalyzeService
from settings import Settings
from api.services.analyze.pipeline.matches import *  # noqa


class AnalyzeMatchesContainer(containers.DeclarativeContainer):
    """ A container that provides the AnalyzeService for matches.

    The container is responsible for providing the AnalyzeService with all of its dependencies.
    """

    config = providers.Configuration(default=Settings().dict())

    repository = providers.Factory(
        CsvRepository,
        context=config.dirs.data,
        data_type=DataType.MATCHES,
    )

    pipeline = providers.List([
        ClearColumnsFromHyphens,
        CreateWinLoseColumns,
        FilterCompletedGamesColumn,
        CreateWinnerColumn,
        ClearTeams,
    ])

    df_factory = providers.Factory(
        DataFrameFromCSVFactory,
    )

    service = providers.Factory(
        AnalyzeService,
        repository=repository,
        pipeline=pipeline,
        df_factory=df_factory,
    )
