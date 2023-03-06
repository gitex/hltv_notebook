from dependency_injector import providers, containers

from infra.storage.choices import DataType
from api.services.save import StoreDataFrameService
from infra.storage.repositories import CsvRepository
from infra.storage.factories import * # noqa
from settings import Settings


class StoreMatchesToCsvContainer(containers.DeclarativeContainer):
    config = providers.Configuration(default=Settings().dict())

    repository = providers.Factory(
        CsvRepository,
        context=config.dirs.csv_matches,
        data_type=DataType.MATCHES,
    )

    prepare_data = providers.Factory(
        CSVFromDataFrameFactory,
    )

    service = providers.Factory(
        StoreDataFrameService,
        repository=repository,
        prepare_data=prepare_data,
    )
