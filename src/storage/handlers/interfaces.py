from dataclasses import dataclass
from pathlib import Path

from storage.constants import DataType
from storage.stubs import SuccessMessage


@dataclass
class IStorage:
    data_type: DataType
    data_dir: Path | None

    def store(self, data: str) -> SuccessMessage: ...
