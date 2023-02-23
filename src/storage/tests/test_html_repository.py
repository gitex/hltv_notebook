from storage.stubs import Identifier


def test_get_many_html_files(make_html_files_of_matches, matches_html_repository):
    assert matches_html_repository.get_many()


def test_get_one_html_file(make_html_files_of_matches, matches_html_repository):
    file_path = make_html_files_of_matches[0]

    html = matches_html_repository.get_one(identifier=Identifier.from_path(file_path))
    assert html
    assert html == file_path.read_text()


def test_create_html_file(matches_html_repository, matches_html, secret_code):
    matches_html += secret_code

    identifier = matches_html_repository.create(data=matches_html)

    html = matches_html_repository.get_one(identifier)
    assert matches_html == html
