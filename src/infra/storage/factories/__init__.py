from .base import IFactory, CompositeFactory
from .csv import CSVFromDataFrameFactory
from .data_frame import IDataFrameFactory, DataFrameFromCSVFactory, DataFrameFromHTMLFactory


CSVFromHTMLFactory = CompositeFactory([
    DataFrameFromHTMLFactory,
    CSVFromDataFrameFactory,
])
