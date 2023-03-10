from infra.data_frames.pipeline import Pipeline


def test_only_first_handler(first_handler):
    pipeline = Pipeline([first_handler])
    pipeline.fill_dependencies()
    assert pipeline.handlers == [first_handler]


def test_second_handler_without_first(first_handler, second_handler):
    pipeline = Pipeline([second_handler])
    pipeline.fill_dependencies()
    assert pipeline.handlers == [first_handler, second_handler]


def test_second_handler_with_first(first_handler, second_handler):
    pipeline = Pipeline([first_handler, second_handler])
    pipeline.fill_dependencies()
    assert pipeline.handlers == [first_handler, second_handler]


def test_third_without_dependencies(first_handler, second_handler, third_handler):
    pipeline = Pipeline([third_handler])
    pipeline.fill_dependencies()
    assert pipeline.handlers == [first_handler, second_handler, third_handler]


def test_third_with_first_handler(first_handler, second_handler, third_handler):
    pipeline = Pipeline([first_handler, third_handler])
    pipeline.fill_dependencies()
    assert pipeline.handlers == [first_handler, second_handler, third_handler]


def test_second_handler_before_first_one(first_handler, second_handler):
    pipeline = Pipeline([second_handler, first_handler])
    pipeline.fill_dependencies()
    assert pipeline.handlers == [first_handler, second_handler]


def test_third_handler_before_first_one(first_handler, second_handler, third_handler):
    pipeline = Pipeline([third_handler, second_handler, first_handler])
    pipeline.fill_dependencies()
    assert pipeline.handlers == [first_handler, second_handler, third_handler]


def test_third_handler_before_second_one(first_handler, second_handler, third_handler):
    pipeline = Pipeline([third_handler, first_handler, second_handler])
    pipeline.fill_dependencies()
    assert pipeline.handlers == [first_handler, second_handler, third_handler]


def test_fill_from(first_handler, second_handler, third_handler):
    pipeline = Pipeline.fill_from([third_handler, first_handler, second_handler])
    assert pipeline.handlers == [first_handler, second_handler, third_handler]
