import pandas as pd
from lxml.etree import ParseError

from infra.stubs import Html, CSV

from .base import IFactory, In


class IDataFrameFactory(IFactory):
    """ A factory that creates DataFrame. """

    def __call__(self, data: In) -> pd.DataFrame | None:
        ...


class DataFrameFromHTMLFactory(IDataFrameFactory):
    """ A factory that creates DataFrame from HTML."""

    def __call__(self, data: Html) -> pd.DataFrame | None:
        if not data:
            return None

        try:
            df = pd.read_html(data)
        except ParseError:
            return None

        return pd.concat(df)


class DataFrameFromCSVFactory(IDataFrameFactory):
    """ A factory that creates DataFrame from CSV."""

    def __call__(self, data: CSV) -> pd.DataFrame | None:
        if not data:
            return None

        df = pd.read_csv(data)

        return pd.concat(df)
