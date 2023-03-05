from dataclasses import dataclass
import logging

from infra.hltv_client import HLTVClient
from infra.storage.repositories import IRepository
from infra.storage.stubs import SuccessMessage
from infra.storage.factories import IFactory


logger = logging.getLogger('services')


@dataclass
class DownloadMatchesService:
    """ A service that downloads matches from HLTV.

    The service is responsible for downloading matches from HLTV and saving them to the repository.

    Attributes:
        client: A client that is used to download matches from HLTV.
        repository: A repository that is used to save matches.
        repository_input_factory: A factory that is used to create a repository input from the downloaded content.
    """

    client: HLTVClient
    repository: IRepository
    repository_input_factory: IFactory | None

    def download_matches_by_page(self, page: int) -> SuccessMessage:
        """ Downloads matches from a given page and saves them to the repository."""

        logger.info(f'Start download page {page}...')

        response = self.client.get_matches_by_page(page)
        content = self.repository_input_factory(response.content)

        if not content:
            raise ValueError(f'Content is empty: {content!r}')

        success_message = self.repository.create(data=content, page=str(page))
        return success_message

    def download_matches_between_pages(self, start_page: int, end_page: int):
        """ Downloads matches from a given range of pages and saves them to the repository. """

        logger.info(f'Start download pages from {start_page} to {end_page}...')

        for page in range(start_page, end_page + 1):
            self.download_matches_by_page(page)

        return SuccessMessage(f'Pages from {start_page} to {end_page} download successfully!')
