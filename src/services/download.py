from dataclasses import dataclass
import logging

from client import HLTVClient
from storage import IStorage
logger = logging.getLogger('services')


@dataclass
class DownloadMatchesService:
    client: HLTVClient
    storage: IStorage

    def download_matches_by_page(self, page: int):
        logger.info(f'Start download page {page}...')

        response = self.client.get_matches_by_page(page)

        success_message = self.storage.store(response.content)
        logger.info(success_message)

    def download_matches_between_pages(self, start_page: int, end_page: int):
        logger.info(f'Start download pages from {start_page} to {end_page}...')

        for page in range(start_page, end_page + 1):
            self.download_matches_by_page(page)
