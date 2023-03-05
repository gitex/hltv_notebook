from dataclasses import dataclass

import pandas as pd

from infra.storage.repositories import IRepository
from infra.storage.structs import Identifier
from infra.storage.factories.data_frame import IDataFrameFactory

from infra.data_frames.pipeline import Pipeline


@dataclass
class DataFramePipelineService:
    repository: IRepository
    df_factory: IDataFrameFactory
    pipeline: Pipeline

    def collect_all(self) -> pd.DataFrame | None:
        dfs: list[pd.DataFrame] = []

        for data in self.repository.get_many():
            df = self.df_factory(data)

            if df is None:
                continue

            dfs.append(df)

        if not dfs:
            return None

        df = pd.concat(dfs)

        return self.pipeline.handle(df)

    def collect_one(self, identifier: Identifier) -> pd.DataFrame | None:
        data = self.repository.get_one(identifier)

        if data is None:
            return None

        df = self.df_factory(data)

        if df is None:
            return None

        return self.pipeline.handle(df)
