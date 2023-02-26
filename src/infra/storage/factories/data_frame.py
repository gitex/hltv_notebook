import pandas as pd
from lxml.etree import ParseError

from infra.stubs import Html, CSV


class DataFrameFactory:

    @classmethod
    def from_html(cls, html: Html) -> pd.DataFrame | None:
        """ Make DataFrame from Html body. """

        if not html:
            return None

        try:
            df = pd.read_html(html)
        except ParseError:
            return None

        return pd.concat(df)

    @classmethod
    def from_csv(cls, csv: CSV) -> pd.DataFrame | None:
        """ Make DataFrame from CSV body. """

        if not csv:
            return None

        df = pd.read_csv(csv)

        return pd.concat(df)
