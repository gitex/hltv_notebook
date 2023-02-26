from infra.storage.factories import DataFrameFactory, CSVFactory
from infra.stubs import CSV, Html

from .base import ITextFormatter


class HtmlToCsv(ITextFormatter):
    def handle(self, data: Html) -> CSV:
        df = DataFrameFactory.from_html(data)

        return CSVFactory.from_data_frame(df)
