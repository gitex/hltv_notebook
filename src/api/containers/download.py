from dependency_injector import providers, containers

from infra.hltv_client import RequestsHTTPClient
from infra.hltv_client import HLTVClient
from infra.storage.choices import DataType
from api.services.download import DownloadMatchesService
from infra.storage.repositories import HtmlRepository
from infra.storage.formatters import HtmlToCsv
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

    formatter = providers.Factory(
        HtmlToCsv,
    )

    service = providers.Factory(
        DownloadMatchesService,
        client=hltv_client,
        repository=repository,
        formatter=formatter,
    )
