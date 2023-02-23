from storage.repositories.base import IRepository
from pathlib import Path

from storage.utils import generate_filename
from storage.choices import DataType
from storage.stubs import SuccessMessage

from storage.stubs import URI, Html, Identifier


class BaseFileRepository(IRepository):
    extension: str = NotImplemented

    @property
    def _target_path(self) -> Path:
        return Path(self.context) / self.extension / self.data_type

    def _find_in_target_path(self, identifier: str) -> list[Path]:
        return list(self._target_path.glob(f'{identifier}.{self.extension}'))

    def prepare(self) -> SuccessMessage:
        """ Create parent directory. """

        self._target_path.mkdir(parents=True, exist_ok=True)
        return SuccessMessage(f'Directory {self._target_path} was created successfully!')

    def get_one(self, identifier: Identifier) -> Html | None:
        files = self._target_path.glob(f'{identifier}.{self.extension}')

        try:
            return Html(next(files).read_text())
        except StopIteration:
            return None

    def get_many(self) -> list[Html]:
        files = self._target_path.glob(f'*.{self.extension}')

        return [Html(path.read_text()) for path in files]

    def create(self, data: str) -> Identifier:
        """ Create file and return name. """

        path = self._target_path / generate_filename(self.extension)
        path.write_text(data)

        return Identifier(path.stem)


class HtmlRepository(BaseFileRepository):
    extension = 'html'


class CsvRepository(BaseFileRepository):
    extension = 'csv'
