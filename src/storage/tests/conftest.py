from pathlib import Path
from uuid import uuid4

import pytest

from storage import generate_filename, HtmlRepository, DataType
from client.http_client import Response, Html


@pytest.fixture(scope='session')
def example_dir() -> Path:
    return Path(__file__).parent / 'examples'


@pytest.fixture(scope='session')
def matches_html(example_dir) -> Html:
    with open(example_dir / 'matches.html') as f:
        html = f.read()

    return Html(html)


@pytest.fixture
def matches_response(matches_html) -> Response:
    return Response(
        ok=True,
        status_code=200,
        data={},
        content=Html(matches_html),
    )


@pytest.fixture(scope='session')
def data_dir(tmp_path_factory) -> Path:
    return tmp_path_factory.mktemp("data")


@pytest.fixture(scope='session')
def html_dir(data_dir) -> Path:
    path = data_dir / 'html'
    path.mkdir(exist_ok=True)
    return path


@pytest.fixture(scope='session')
def matches_dir(html_dir) -> Path:
    path = html_dir / 'matches'
    path.mkdir(exist_ok=True)
    return path


@pytest.fixture(scope='session')
def make_html_files_of_matches(matches_dir, matches_html) -> list[Path]:
    html_files: list[Path] = []

    for _ in range(5):
        path = matches_dir / generate_filename('html')
        html_files.append(path)
        path.write_text(matches_html)

    return html_files


@pytest.fixture(scope='session')
def matches_html_repository(data_dir) -> HtmlRepository:
    return HtmlRepository(context=data_dir, data_type=DataType.MATCHES)


@pytest.fixture
def mock_repository(mocker):
    return mocker.Mock()


@pytest.fixture
def secret_code() -> str:
    return str(uuid4())
