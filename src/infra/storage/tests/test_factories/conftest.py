from typing import Type

import pytest

from src.infra.storage.factories import IFactory


def make_factory(class_name: str) -> Type[IFactory]:
    """ Creates a factory that returns the input data concatenated with the given class name."""
    class Factory(IFactory):
        def __call__(self, data: str) -> str:
            return data + class_name

    Factory.__class__.__name__ = class_name
    return Factory


@pytest.fixture
def a_factory():
    return make_factory('A')


@pytest.fixture
def b_factory():
    return make_factory('B')


@pytest.fixture
def c_factory():
    return make_factory('C')
