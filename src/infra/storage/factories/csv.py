import pandas as pd

from infra.stubs import CSV
from infra.storage.constants import CSV_DELIMITER


class CSVFactory:
    delimiter: str = CSV_DELIMITER

    @classmethod
    def from_data_frame(cls, df: pd.DataFrame) -> CSV:
        return CSV(df.to_csv(index=False, sep=cls.delimiter))
