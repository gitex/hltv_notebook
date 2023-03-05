from infra.storage.repositories.base import IRepository
from pathlib import Path

from infra.storage.stubs import SuccessMessage
from infra.stubs import Html
from infra.storage.structs import Identifier, Filename
from infra.storage.constants import Extension


class BaseFileRepository(IRepository):
    """ A base class for file-based repositories."""

    extension: str = NotImplemented  # The file extension, e.g. 'html', 'csv', etc.
    newline: str = NotImplemented  # The newline character to use when writing files.
    encoding: str = 'utf-8'

    @property
    def _target_path(self) -> Path:
        """ Returns the path to the directory where the files are stored. """
        return Path(self.context) / self.extension / self.data_type

    def _find_in_target_path(self, identifier: str) -> list[Path]:
        """ Returns a list of files that match the given identifier."""
        return list(self._target_path.glob(f'{identifier}.{self.extension}'))

    def prepare(self) -> SuccessMessage:
        """ Create directory if it doesn't exist. """

        self._target_path.mkdir(parents=True, exist_ok=True)
        return SuccessMessage(f'Directory {self._target_path} was created successfully!')

    def get_one(self, identifier: Identifier) -> Html | None:
        """ Returns the file content if it exists. """
        files = self._target_path.glob(f'{identifier}.{self.extension}')

        try:
            return Html(next(files).read_text())
        except StopIteration:
            return None

    def get_many(self) -> list[Html]:
        """ Return content of all files."""
        files = self._target_path.glob(f'*.{self.extension}')

        return [Html(path.read_text()) for path in files]

    def create(self, data: str, page: str = None) -> Identifier:
        """ Create file and return name. """

        filename = Filename.generate_on_current_datetime(
            extension=self.extension,
            suffix=page,
        )

        path = self._target_path / str(filename)
        path.write_text(data, newline=self.newline, encoding=self.encoding)

        return Identifier(path.stem)


class HtmlRepository(BaseFileRepository):
    """ A repository for storing HTML files."""

    extension = Extension.HTML
    newline = '\n'


class CsvRepository(BaseFileRepository):
    """ A repository for storing CSV files."""

    extension = Extension.CSV
    newline = ''
