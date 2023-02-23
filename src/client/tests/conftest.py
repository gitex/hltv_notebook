import pytest
from pathlib import Path
from client.http_client import Response


EXAMPLES_DIR = Path(__file__) / 'examples'


@pytest.fixture
def matches_html() -> str:
    with open(EXAMPLES_DIR / 'matches.html') as f:
        html = f.read()

    return html


@pytest.fixture
def matches_response(matches_html) -> Response:
    return Response(
        ok=True,
        status_code=200,
        data={},
        content=matches_html,
    )
