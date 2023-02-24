from dependency_injector import providers, containers

from client.http_client import RequestsHTTPClient
from client import HLTVClient
from storage.choices import DataType
from services.download import DownloadMatchesService
from storage.repositories import HtmlRepository
from settings import Settings


class DownloadMatchesContainer(containers.DeclarativeContainer):
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
        HtmlRepository,
        context=config.dirs.data,
        data_type=DataType.MATCHES,
    )

    service = providers.Factory(
        DownloadMatchesService,
        client=hltv_client,
        repository=repository,
    )
