from infra.storage.factories import CompositeFactory, IFactory


def test_composite_factory_with_three_fixtures_applies_sequentially(a_factory, b_factory, c_factory):
    composite_factory = CompositeFactory([a_factory, b_factory, c_factory])

    assert composite_factory('') == 'ABC'


def test_composite_factory_with_two_fixtures_applies_sequentially(a_factory, b_factory):
    composite_factory = CompositeFactory([a_factory, b_factory])

    assert composite_factory('') == 'AB'


def test_composite_factory_returns_none_if_any_factory_returns_none(a_factory, b_factory, c_factory):
    class B(IFactory):
        def __call__(self, data: str) -> str | None:
            return None

    composite_factory = CompositeFactory([a_factory, B, c_factory])

    assert composite_factory('') is None


def test_composite_factory_with_no_fixtures_returns_input_data():
    composite_factory = CompositeFactory([])

    assert composite_factory('') == ''


def test_composite_factory_with_one_fixture_returns_input_data():
    class A(IFactory):
        def __call__(self, data: str) -> str:
            return data

    composite_factory = CompositeFactory([A])

    assert composite_factory('') == ''
