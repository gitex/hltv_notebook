import abc
from typing import Self, Type, NewType
from dataclasses import dataclass, field

import pandas as pd

from .exceptions import PipelineException


class Handler(abc.ABC):
    depends_on: Type[Self] | None

    @abc.abstractmethod
    def handle(self, df: pd.DataFrame) -> pd.DataFrame: ...

    @classmethod
    def dependencies(cls) -> list[Type['Handler']]:
        handlers: list[Type[Handler]] = []

        if not cls.depends_on:
            return handlers

        next_handler: Type[Handler] = cls.depends_on

        while next_handler:
            handlers.append(next_handler)

            next_handler = next_handler.depends_on

        return handlers[::-1]

    def __hash__(self):
        return hash(self.__class__.__name__)


@dataclass
class Pipeline:
    handlers: list[Type[Handler]]

    __dependencies_filled: bool = field(init=False, default=False)

    def fill_dependencies(self) -> None:
        handlers: list[Type[Handler]] = []

        for handler in self.handlers:
            if handler in handlers:
                continue

            dependencies = handler.dependencies()
            for dependency in dependencies:
                if dependency not in handlers:
                    handlers.append(dependency)

            handlers.append(handler)

        self.handlers = list(handlers)
        self.__dependencies_filled = True

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        if not self.__dependencies_filled:
            raise PipelineException('Pipeline should be fill with dependencies.')

        for handler in self.handlers:
            df = handler().handle(df)

        return df
