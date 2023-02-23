from dataclasses import dataclass
import logging

from storage.utils import generate_filename
from storage.constants import DataType
from settings import DATA_DIR

from .interfaces import IStorageHandler


HTML_DIR = DATA_DIR / 'html'


logger = logging.getLogger('storage')


@dataclass
class FileHandler(IStorageHandler):
    data: str
    data_type: DataType

    def store(self) -> None:
        target_dir = HTML_DIR / self.data_type.value
        target_file = target_dir / generate_filename('html')

        with open(target_file, 'w') as f:
            f.write(self.data)

        logger.debug(f'Data was saved into {target_file.absolute()}')
