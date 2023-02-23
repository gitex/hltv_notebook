from dependency_injector import providers, containers

from client.http_client import RequestsHTTPClient
from client import HLTVClient
from storage.choices import DataType
from services.download import DownloadMatchesService
from storage.repositories import HtmlRepository


class DownloadMatchesContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=[
            'services', 'src.services',
        ],
    )

    config = providers.Configuration()

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
        data_type=DataType.MATCHES,
        data_dir=config.dirs.html,
    )

    service = providers.Factory(
        DownloadMatchesService,
        client=hltv_client,
        repository=repository,
    )
