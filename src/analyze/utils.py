import re
from functools import partial
from typing import Generator, Optional
import itertools

import pandas as pd


def match(pattern: re.Pattern, value: str) -> str:
    return re.search(pattern, value).group(1)


def make_column(df: pd.DataFrame, column_name: str, on_column: str, pattern: re.Pattern):
    match_on_pattern = partial(match, pattern)
    df[column_name] = list(map(match_on_pattern, df[on_column].tolist()))
    return df


def possible_final_scores() -> Generator[int, None, None]:
    yield from itertools.count(start=16, step=3)


def score_is_final(score: int) -> bool:
    for possible_score in possible_final_scores():
        if score == possible_score:
            return True

        if score > possible_score:
            break

    return False
