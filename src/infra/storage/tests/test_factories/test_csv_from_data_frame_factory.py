import pytest
import pandas as pd

from infra.storage.factories import CSVFromDataFrameFactory
from infra.stubs import CSV


@pytest.fixture
def csv_from_data_frame_factory():
    return CSVFromDataFrameFactory()


def test_csv_from_data_frame_factory(csv_from_data_frame_factory, data_frame):
    csv = csv_from_data_frame_factory(data_frame)

    assert csv == CSV('a,b\r\n1,2\r\n3,4\r\n')


def test_csv_from_data_frame_factory_with_empty_data_frame(csv_from_data_frame_factory):
    csv = csv_from_data_frame_factory(pd.DataFrame())

    assert csv == CSV('')


def test_csv_from_data_frame_factory_with_none_data_frame(csv_from_data_frame_factory):
    csv = csv_from_data_frame_factory(None)

    assert csv is None


def test_csv_from_data_frame_factory_with_invalid_data_frame(csv_from_data_frame_factory):
    csv = csv_from_data_frame_factory('invalid')

    assert csv is None
