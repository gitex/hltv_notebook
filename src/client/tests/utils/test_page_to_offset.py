import pytest

from client.utils import get_offset_by_page


@pytest.mark.parametrize(
    'page,expected_offset',
    (
        (0, 0),
        (1, 0),
        (2, 50),
        (3, 100),
        (4, 150),
    )
)
def test_date(page: int, expected_offset: int):
    assert get_offset_by_page(page) == expected_offset
