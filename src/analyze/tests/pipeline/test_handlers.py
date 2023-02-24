from analyze.pipeline import Pipeline, Handler as OriginalHandler
import pandas as pd


def test_dependencies():
    class Handler(OriginalHandler):
        def handle(self, df: pd.DataFrame) -> pd.DataFrame:
            return df

    class FirstHandler(Handler):
        depends_on = None

    class SecondHandler(Handler):
        depends_on = FirstHandler

    class ThirdHandler(Handler):
        depends_on = SecondHandler

    assert FirstHandler.dependencies() == []
    assert SecondHandler.dependencies() == [FirstHandler]
    assert ThirdHandler.dependencies() == [FirstHandler, SecondHandler]
