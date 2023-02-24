import pandas as pd
from lxml.etree import ParseError

from storage import Html


def df_from_html(html: Html) -> pd.DataFrame | None:
    if not html:
        return None

    # Make DataFrame from html
    try:
        df = pd.read_html(html)
    except ParseError:
        return None

    # Join all rows in one DataFrames
    return pd.concat(df)
