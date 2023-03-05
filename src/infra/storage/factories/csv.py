import pandas as pd

from infra.stubs import CSV, Html
from infra.storage.constants import CSV_DELIMITER

from .base import IFactory, In


class ICSVFactory(IFactory):
    """ A factory that creates CSV. """

    def __call__(self, data: In) -> CSV | None:
        ...


class CSVFromDataFrameFactory(ICSVFactory):
    """ A factory that creates CSV from a DataFrame. """

    def __call__(self, data: pd.DataFrame) -> CSV | None:
        return CSV(data.to_csv(index=False, sep=CSV_DELIMITER))
