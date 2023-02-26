from datetime import date, datetime

from .constants import QUERY_DATE_FORMAT


def get_offset_by_page(page: int) -> int:
    if page < 1:
        return 0

    return (page - 1) * 50


def date_as_query(dt: date | datetime) -> str:
    if isinstance(dt, datetime):
        dt = dt.date()

    return dt.strftime(QUERY_DATE_FORMAT)
