from dataclasses import dataclass

import pandas as pd

from storage import IRepository, Identifier
from services.utils import df_from_html
from .pipeline import Pipeline


@dataclass
class AnalyzeService:
    repository: IRepository
    pipeline: Pipeline

    def collect_all(self) -> pd.DataFrame | None:
        data_frames: list[pd.DataFrame] = []

        for html in self.repository.get_many():
            df = df_from_html(html)

            if df is None:
                continue

            data_frames.append(df)

        if not data_frames:
            return None
        return pd.concat(data_frames)

    def collect_one(self, identifier: Identifier) -> pd.DataFrame | None:
        html = self.repository.get_one(identifier)

        if not html:
            return None
        return df_from_html(html)
