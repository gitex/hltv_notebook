from ..constants import CSV_DELIMITER, CSV_NEWLINE


class CsvMixin:
    """ A mixin that provides CSV constants. """

    def __init__(self, header: bool = True, delimiter: str = CSV_DELIMITER):
        self._header = header
        self._delimiter = delimiter
