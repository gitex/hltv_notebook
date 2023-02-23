from dependency_injector import providers, containers

from client.http_client import RequestsHTTPClient
from client import HLTVClient
from storage import FileStorage, DataType
from services.download import DownloadMatchesService


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

    storage = providers.Factory(
        FileStorage,
        data_type=DataType.MATCHES,
        data_dir=config.dirs.html,
    )

    service = providers.Factory(
        DownloadMatchesService,
        client=hltv_client,
        storage=storage,
    )
