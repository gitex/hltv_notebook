from typing import NewType
from pathlib import Path
from uuid import uuid4
from datetime import datetime


SuccessMessage = NewType('SuccessMessage', str)
URI = NewType('URI', str)
Html = NewType('Html', str)


class Identifier(str):

    @classmethod
    def from_path(cls, path: Path) -> 'Identifier':
        return cls(path.stem)

    @classmethod
    def from_uuid(cls) -> 'Identifier':
        return cls(uuid4())

    @classmethod
    def from_filename(cls) -> 'Identifier':
        return cls(datetime.utcnow().strftime('%d%m%Y_%H%M%S'))
