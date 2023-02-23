import logging
from json import JSONDecodeError
import requests

from .base import IHTTPClient, Response

logger = logging.getLogger('http_client')

class HTTPClient(IHTTPClient):
    def __init__(self, base_url: str, headers: dict | None = None, cookies: dict | None = None, proxy: str = '',
                 verify_certificate: bool = True):
        super().__init__(base_url, headers, cookies, proxy, verify_certificate)
        self.base_url = base_url

        self.__headers = headers or {}
        self.__cookies = cookies or {}
        self.__verify_certificate = verify_certificate

        self.__proxies = {}

        if proxy and isinstance(proxy, str):
            self.__proxies.update(
                {
                    'http_client': proxy,
                    'https': proxy,
                },
            )

    def _build_absolute_url(self, uri: str) -> str:
        return ''.join([self.base_url, uri])  # urljoin not working with x5 url

    def _prepare_headers(self, headers: dict | None) -> dict:
        headers = headers or {}
        return {**self.__headers, **headers}

    def _prepare_cookies(self, cookies: dict | None) -> dict:
        cookies = cookies or {}
        return {**self.__cookies, **cookies}

    @property
    def headers(self) -> dict:
        return self.__headers

    @headers.setter
    def headers(self, headers: dict):  # type: ignore
        self.__headers = headers

    @property
    def cookies(self) -> dict:
        return self.__cookies

    @cookies.setter
    def cookies(self, cookies: dict):  # type: ignore
        self.__cookies = cookies

    def request(
            self,
            method: str,
            url: str,
            params: dict | None = None,
            data: dict | None = None,
            json: dict | None = None,
            headers: dict | None = None,
            cookies: dict | None = None,
            files: dict | None = None,
            verify: bool | None = True,
    ) -> Response:

        logger.debug(f'Request to {self._build_absolute_url(url)!r} with data {data or json}...')

        response: requests.Response = requests.request(
            method,
            self._build_absolute_url(url),
            params=params,
            data=data,
            json=json,
            files=files,
            headers=self._prepare_headers(headers),
            cookies=self._prepare_cookies(cookies),
            proxies=self.__proxies,
            verify=self.__verify_certificate,
        )

        response_json = self._parse_json_response(response)

        logger.debug(
            f'Response from {response.request.url} [{response.status_code}]: '  # type: ignore
            f'{response_json or response.content}',
        )

        return Response(
            ok=response.ok,
            data=response_json,
            content=response.content,
            status_code=response.status_code,
        )

    @staticmethod
    def _parse_json_response(response: requests.Response) -> dict:
        try:
            return response.json()
        except JSONDecodeError:
            return {}
