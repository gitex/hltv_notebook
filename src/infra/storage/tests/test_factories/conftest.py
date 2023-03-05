from typing import Type

import pytest
import pandas as pd

from infra.storage.factories import IFactory


def make_factory(class_name: str) -> Type[IFactory]:
    """ Creates a factory that returns the input data concatenated with the given class name."""
    class Factory(IFactory):
        def __call__(self, data: str) -> str:
            return data + class_name

    Factory.__class__.__name__ = class_name
    return Factory


@pytest.fixture(scope='session')
def a_factory():
    return make_factory('A')


@pytest.fixture(scope='session')
def b_factory():
    return make_factory('B')


@pytest.fixture(scope='session')
def c_factory():
    return make_factory('C')


@pytest.fixture(scope='session')
def data_headers():
    return ['a', 'b']


@pytest.fixture(scope='session')
def data_values():
    return [[1, 2], [3, 4]]


@pytest.fixture
def data_frame(data_headers, data_values):
    return pd.DataFrame(data_values, columns=data_headers)
