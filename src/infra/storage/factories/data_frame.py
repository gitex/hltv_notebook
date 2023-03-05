from io import StringIO

import pandas as pd
from lxml.etree import ParseError

from infra.stubs import Html, CSV

from ..constants import CSV_NEWLINE, CSV_DELIMITER

from .base import IFactory, In
from .mixins import CsvMixin


class IDataFrameFactory(IFactory):
    """ A factory that creates DataFrame. """

    def __call__(self, data: In) -> pd.DataFrame | None:
        """ Creates a DataFrame from the given data. """
        ...


class DataFrameFromHTMLFactory(IDataFrameFactory):
    """ A factory that creates DataFrame from HTML."""

    def __call__(self, data: Html) -> pd.DataFrame | None:
        if not data:
            return pd.DataFrame()

        try:
            df = pd.read_html(data)
        except ParseError:
            return None

        return pd.concat(df)


class DataFrameFromCSVFactory(IDataFrameFactory, CsvMixin):
    """ A factory that creates DataFrame from CSV. """

    def __call__(self, data: CSV) -> pd.DataFrame | None:
        if not data:
            return pd.DataFrame()

        try:
            data = StringIO(data)
        except TypeError:
            return None

        try:
            df = pd.read_csv(data, delimiter=self._delimiter)
        except ValueError:
            return None

        return df
