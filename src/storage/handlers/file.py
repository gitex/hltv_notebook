from dataclasses import dataclass
import logging
from pathlib import Path

from storage.utils import generate_filename
from storage.constants import DataType
from storage.stubs import SuccessMessage

from .interfaces import IStorage


logger = logging.getLogger('storage')


@dataclass
class FileStorage(IStorage):
    data_type: DataType
    data_dir: Path

    def store(self, data: str) -> SuccessMessage:
        target_file = self.data_dir / self.data_type.value / generate_filename('html')

        with open(target_file, 'wb') as f:
            f.write(data.encode())

        return SuccessMessage(f'Successfully stored into {target_file}')
