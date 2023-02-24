import pytest

from containers import analyze_container as original_analyze_container


@pytest.fixture
def analyze_container(matches_html_repository):
    original_analyze_container.repository.override(matches_html_repository)

    return original_analyze_container


@pytest.fixture
def download_matches_container(matches_html_repository):
    original_analyze_container.repository.override(matches_html_repository)

    return original_analyze_container
