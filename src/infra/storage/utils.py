from datetime import datetime

import pandas as pd
from lxml.etree import ParseError

from infra.exceptions import InfraError

from .constants import EXTENSION_DELIMITER
from ..stubs import Html


def generate_filename_on_current_datetime(delimiter: str = '-') -> str:
    """ Generate filename based on current datetime. """

    now = datetime.utcnow()

    return delimiter.join([
        now.date().strftime('%d%m%Y'),
        now.time().strftime('%H%M%S'),
    ])


def clear_extension(extension: str) -> str:
    """ Clear extension from dots. """

    return extension.strip(EXTENSION_DELIMITER)


def df_from_html(html: Html) -> pd.DataFrame | None:
    if not html:
        return None

    try:
        df = pd.read_html(html)
    except ParseError:
        return None

    return pd.concat(df)
