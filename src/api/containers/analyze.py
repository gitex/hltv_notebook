from dependency_injector import providers, containers

from infra.storage import DataType, HtmlRepository
from api.services import AnalyzeService
from settings import Settings


class AnalyzeMatchesContainer(containers.DeclarativeContainer):
    config = providers.Configuration(default=Settings().dict())

    repository = providers.Factory(
        HtmlRepository,
        context=config.dirs.data,
        data_type=DataType.MATCHES,
    )

    service = providers.Factory(
        AnalyzeService,
        repository=repository,
    )
