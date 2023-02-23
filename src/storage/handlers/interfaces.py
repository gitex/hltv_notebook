from dataclasses import dataclass
from storage.constants import DataType


@dataclass
class IStorageHandler:
    data: str
    data_type: DataType

    def store(self) -> None: ...
