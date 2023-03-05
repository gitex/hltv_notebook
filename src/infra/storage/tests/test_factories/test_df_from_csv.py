import pytest
import pandas as pd

from infra.storage.factories import DataFrameFromCSVFactory


@pytest.fixture(scope='module')
def data_frame_from_csv_factory():
    return DataFrameFromCSVFactory()


def test_data_frame_from_csv_factory(data_frame_from_csv_factory, csv, csv_values, csv_headers):
    data_frame = data_frame_from_csv_factory(csv)

    assert data_frame is not None
    assert data_frame.equals(pd.DataFrame(csv_values, columns=csv_headers))


def test_data_frame_from_csv_factory_with_empty_csv(data_frame_from_csv_factory):
    data_frame = data_frame_from_csv_factory('')

    assert data_frame is not None
    assert data_frame.empty


def test_data_frame_from_csv_factory_with_none_csv(data_frame_from_csv_factory):
    data_frame = data_frame_from_csv_factory(None)

    assert data_frame is not None
    assert data_frame.empty


def test_data_frame_from_csv_factory_with_invalid_csv(data_frame_from_csv_factory):
    data_frame = data_frame_from_csv_factory(1)

    assert data_frame is None
