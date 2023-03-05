import re
from functools import partial

import pandas as pd


def match(pattern: re.Pattern, value: str) -> str:
    return re.search(pattern, value).group(1)


def make_column(df: pd.DataFrame, column_name: str, on_column: str, pattern: re.Pattern):
    match_on_pattern = partial(match, pattern)
    df[column_name] = list(map(match_on_pattern, df[on_column].tolist()))
    return df
