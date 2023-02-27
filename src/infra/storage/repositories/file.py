from infra.storage.repositories.base import IRepository
from pathlib import Path

from infra.storage.stubs import SuccessMessage
from infra.stubs import Html
from infra.storage.structs import Identifier, Filename


class BaseFileRepository(IRepository):
    extension: str = NotImplemented
    newline: str = NotImplemented
    encoding: str = 'utf-8'

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
    extension = 'html'
    newline = '\n'


class CsvRepository(BaseFileRepository):
    extension = 'csv'
    newline = ''
