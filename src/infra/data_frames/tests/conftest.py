from typing import Type

import pytest
import pandas as pd

from infra.data_frames.pipeline import Handler


@pytest.fixture
def df() -> pd.DataFrame:
    return pd.DataFrame({
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
        "Experience": [2, 12, 40],
    })


@pytest.fixture
def first_handler_result(df) -> pd.DataFrame:
    df["First work at"] = df["Age"] - df["Experience"]
    return df.copy()


@pytest.fixture
def first_handler(first_handler_result) -> Type[Handler]:
    class FirstHandler(Handler):
        depends_on = None

        def handle(self, df: pd.DataFrame) -> pd.DataFrame:
            return first_handler_result

    return FirstHandler


@pytest.fixture
def second_handler_result(first_handler_result) -> pd.DataFrame:
    df = first_handler_result
    df["Diff of 18"] = df["First work at"] - 18
    return df


@pytest.fixture
def second_handler(first_handler: Handler, second_handler_result) -> Type[Handler]:
    class SecondHandler(Handler):
        depends_on = first_handler

        def handle(self, df: pd.DataFrame) -> pd.DataFrame:
            return second_handler_result

    return SecondHandler


@pytest.fixture
def third_handler_result(second_handler_result) -> pd.DataFrame:
    df = second_handler_result
    df["Best age for now"] = df["Age"] - df["Diff of 18"]
    return df


@pytest.fixture
def third_handler(second_handler, third_handler_result) -> Type[Handler]:
    class ThirdHandler(Handler):
        depends_on = second_handler

        def handle(self, df: pd.DataFrame) -> pd.DataFrame:
            return third_handler_result

    return ThirdHandler
