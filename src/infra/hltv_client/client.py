from dataclasses import dataclass

from infra.hltv_client.http_client import IHTTPClient, Method, Response
from infra.hltv_client.utils import get_offset_by_page


@dataclass
class HLTVClient:
    http_client: IHTTPClient

    def get_matches_by_page(self, page: int) -> Response:
        """ Get matches for single page. """

        offset = get_offset_by_page(page)

        return self.http_client.request(
            method=Method.GET,
            url=f'/stats/matches?startDate=all&offset={offset}',
        )
