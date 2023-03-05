from dependency_injector import providers, containers

from infra.storage import DataType, HtmlRepository
from api.services import AnalyzeService
from settings import Settings
from api.services.analyze.pipeline.matches import *  # noqa


class AnalyzeMatchesContainer(containers.DeclarativeContainer):
    config = providers.Configuration(default=Settings().dict())

    repository = providers.Factory(
        HtmlRepository,
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

    service = providers.Factory(
        AnalyzeService,
        repository=repository,
        pipeline=pipeline,
    )
