from dataclasses import dataclass
from pathlib import Path
import logging

import pandas as pd

from infra.storage.repositories import IRepository
from infra.storage.stubs import SuccessMessage
from infra.storage.factories import IFactory


logger = logging.getLogger('services')


@dataclass
class StoreDataFrameService:
    prepare_data: IFactory
    repository: IRepository

    def save(self, df: pd.DataFrame) -> SuccessMessage:
        data = self.prepare_data(df)

        return self.repository.create(data=data)
