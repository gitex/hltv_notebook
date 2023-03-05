from api.containers import analyze_container as original_analyze_container
from infra.storage.tests.conftest import *  # noqa
from infra.storage.factories import *  # noqa


@pytest.fixture
def analyze_container(matches_html_repository):
    original_analyze_container.repository.override(matches_html_repository)

    return original_analyze_container


@pytest.fixture
def analyze_matches_from_html_container(matches_html_repository):
    original_analyze_container.repository.override(matches_html_repository)
    original_analyze_container.df_factory.override(DataFrameFromHTMLFactory())
    return original_analyze_container


@pytest.fixture
def download_matches_container(matches_html_repository):
    original_analyze_container.repository.override(matches_html_repository)

    return original_analyze_container
