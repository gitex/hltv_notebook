from pathlib import Path
from uuid import uuid4
from dataclasses import dataclass

from infra.storage.constants import EXTENSION_DELIMITER
from infra.storage.utils import generate_filename_on_current_datetime, clear_extension


class Identifier(str):

    @classmethod
    def from_path(cls, path: Path) -> 'Identifier':
        return cls(path.stem)

    @classmethod
    def from_uuid(cls) -> 'Identifier':
        return cls(uuid4())


@dataclass(frozen=True, kw_only=True)
class Filename:
    name: str
    extension: str

    def __str__(self):
        return EXTENSION_DELIMITER.join([self.name, self.extension])

    def as_identifier(self) -> Identifier:
        return Identifier(self)

    def as_str(self) -> str:
        return str(self)

    @classmethod
    def generate_on_current_datetime(cls, extension: str, suffix: str = '', delimiter: str = '_') -> 'Filename':
        name = generate_filename_on_current_datetime(delimiter)

        if suffix:
            name = delimiter.join([name, suffix])

        return cls(name=name, extension=clear_extension(extension))

    @classmethod
    def from_path(cls, path: Path) -> 'Filename':
        return cls(name=path.stem, extension=clear_extension(path.suffix))
