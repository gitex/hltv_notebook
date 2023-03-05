from dataclasses import dataclass

import pandas as pd

from infra.storage.repositories import IRepository
from infra.storage.structs import Identifier
from infra.storage.factories.data_frame import IDataFrameFactory

from .pipeline import Pipeline


@dataclass
class AnalyzeService:
    repository: IRepository
    pipeline: Pipeline
    df_factory: IDataFrameFactory

    def collect_all(self) -> pd.DataFrame | None:
        data_frames: list[pd.DataFrame] = []

        for data in self.repository.get_many():
            df = self.df_factory(data)

            if df is None:
                continue

            data_frames.append(df)

        if not data_frames:
            return None
        return pd.concat(data_frames)

    def collect_one(self, identifier: Identifier) -> pd.DataFrame | None:
        data = self.repository.get_one(identifier)

        if not data:
            return None
        return self.df_factory(data)
