from dataclasses import dataclass
from typing import Protocol


@dataclass
class Response:
    ok: bool
    status_code: int
    data: dict
    content: str


class Method:
    GET = 'GET'
    POST = 'POST'


class IHTTPClient(Protocol):
    def __init__(
        self,
        base_url: str,
        headers: dict | None = None,
        cookies: dict | None = None,
        proxy: str = '',
        verify_certificate: bool = True,
    ):
        ...

    @property
    def headers(self) -> dict:
        raise NotImplementedError()

    @headers.setter
    def headers(self, headers: dict) -> dict:
        raise NotImplementedError()

    @property
    def cookies(self) -> dict:
        raise NotImplementedError()

    @cookies.setter
    def cookies(self, cookies: dict) -> dict:
        raise NotImplementedError()

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
        ...
