from client.http_client import IHTTPClient, HTTPClient, Method, Response
from client.utils import get_offset_by_page


class HLTVClient:
    http_client_type: IHTTPClient = HTTPClient

    def __init__(self, base_url: str, proxy: str = ''):
        self._base_url = base_url
        self._proxy = proxy

    @property
    def http_client(self) -> IHTTPClient:
        return self.http_client_type(base_url=self._base_url, proxy=self._proxy)

    def get_matches_by_page(self, page: int) -> Response:
        """ Get matches for single page. """

        offset = get_offset_by_page(page)

        return self.http_client.request(
            method=Method.GET,
            url=f'/stats/matches?startDate=all&offset={offset}',
        )
