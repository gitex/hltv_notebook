from analyze.pipeline import Pipeline


def test_first_handler_have_not_depends(first_handler):
    assert first_handler.dependencies() == []


def test_second_handler_has_one_dependency(first_handler, second_handler):
    assert second_handler.dependencies() == [first_handler]


def test_third_handler_has_two_dependencies(first_handler, second_handler, third_handler):
    assert third_handler.dependencies() == [first_handler, second_handler]
