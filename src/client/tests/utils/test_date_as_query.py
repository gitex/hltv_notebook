import pytest
from datetime import date, datetime

from client.utils import date_as_query


@pytest.mark.parametrize(
    'dt,expected_result',
    (
        # Date
        (date(2022, 1, 1), '2022-01-01'),
        (date(2000, 12, 1), '2000-12-01'),

        # Datetime
        (datetime(2022, 1, 1, 1, 0, 0), '2022-01-01'),
        (datetime(2022, 12, 5, 1, 0, 0), '2022-12-05'),
        (datetime(2022, 10, 10, 1, 0, 0), '2022-10-10'),
    )
)
def test_date(dt: date | datetime, expected_result: str):
    assert date_as_query(dt) == expected_result

