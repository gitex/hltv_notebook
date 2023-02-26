from infra.stubs import Html


def test_collect_folder_with_files(analyze_container, matches_html, mock_repository):
    mock_repository.get_many.return_value = [Html(matches_html), Html(matches_html)]

    with analyze_container.repository.override(mock_repository):
        service = analyze_container.service()
        assert service.collect_all() is not None


def test_collect_folder_with_empty_files(analyze_container, mock_repository):
    mock_repository.get_many.return_value = [Html(''), Html('')]

    with analyze_container.repository.override(mock_repository):
        service = analyze_container.service()
        assert service.collect_all() is None


def test_collect_folder_without_files(analyze_container, mock_repository):
    mock_repository.get_many.return_value = []

    with analyze_container.repository.override(mock_repository):
        service = analyze_container.service()
        assert service.collect_all() is None
