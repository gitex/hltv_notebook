from dependency_injector import providers, containers

from infra.hltv_client import RequestsHTTPClient
from infra.hltv_client import HLTVClient
from infra.storage.choices import DataType
from api.services.download import DownloadMatchesService
from infra.storage.repositories import CsvRepository
from infra.storage.factories import * # noqa
from settings import Settings


class DownloadMatchesContainer(containers.DeclarativeContainer):
    """ A container that provides the DownloadMatchesService for matches.

    The container is responsible for providing the DownloadMatchesService with all of its dependencies.
    """

    config = providers.Configuration(default=Settings().dict())

    http_client = providers.Factory(
        RequestsHTTPClient,
        base_url=config.hltv.base_url,
        proxy='',
    )

    hltv_client = providers.Factory(
        HLTVClient,
        http_client=http_client,
    )

    repository = providers.Factory(
        CsvRepository,
        context=config.dirs.data,
        data_type=DataType.MATCHES,
    )

    repository_input_factory = providers.Factory(
        CSVFromHTMLFactory,
    )

    service = providers.Factory(
        DownloadMatchesService,
        client=hltv_client,
        repository=repository,
        repository_input_factory=repository_input_factory,
    )
