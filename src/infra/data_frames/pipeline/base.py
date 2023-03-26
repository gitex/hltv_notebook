import abc
from typing import Self, Type, TypeVar
from dataclasses import dataclass, field

import pandas as pd

from .exceptions import PipelineException


class Handler(abc.ABC):
    """ A handler that handles a DataFrame.

    Handlers are used to process a DataFrame in a pipeline.
    Handlers can depend on other handlers, which will be executed before the handler itself.
    """

    depends_on: Type[Self] | None  # Depends on another handler

    @abc.abstractmethod
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        """ Handles a DataFrame. """
        ...

    @classmethod
    def dependencies(cls) -> list[Type['Handler']]:
        """ Returns a list of dependencies for the handler.

        The list is ordered from the lest dependent handler to the most dependent.


        Example:
            class A(Handler):
                pass

            class B(Handler):
                depends_on = A

            class C(Handler):
                depends_on = B

            C.dependencies() -> [A, B]
        """

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


Handlers = TypeVar('Handlers', bound=list[Type[Handler]])


@dataclass
class Pipeline:
    handlers: Handlers

    __dependencies_filled: bool = field(init=False, default=False)

    def fill_dependencies(self) -> None:
        """ Fills the pipeline with dependencies.

        The pipeline will be filled with dependencies in the order of the least dependent handler to the most dependent.

        Example:
            >>> class A(Handler):
            >>>     pass

            >>> class B(Handler):
            >>>     depends_on = A

            >>> class C(Handler):
            >>>     depends_on = B

            >>> pipeline = Pipeline([C, A])
            >>> pipeline.fill_dependencies()
            >>> pipeline.handlers
            [A, B, C]
        """

        if self.__dependencies_filled:
            return

        handlers: Handlers = []

        for handler in self.handlers:
            if handler in handlers:
                continue

            dependencies = handler.dependencies()

            for dependency in dependencies:
                if dependency in handlers:
                    continue

                handlers.append(dependency)

            handlers.append(handler)

        self.handlers = list(handlers)
        self.__dependencies_filled = True

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        """ Handles a DataFrame. """

        self.validate()

        for handler_type in self.handlers:
            if callable(handler_type):
                handler = handler_type()
            else:
                handler = handler_type

            df = handler.handle(df)

        return df

    @classmethod
    def fill_from(cls, handlers: Handlers) -> 'Pipeline':
        """ Fills the pipeline with dependencies.

        Example:
            >>> class A(Handler):
            >>>    pass

            >>> class B(Handler):
            >>>    depends_on = A

            >>> pipeline = Pipeline.fill_from([B])
            >>> pipeline.handlers
            [A, B]
        """

        pipeline = cls(handlers)
        pipeline.fill_dependencies()
        pipeline.validate()
        return pipeline

    def validate(self) -> None:
        """ Validates the pipeline dependencies.

        Raises:
            PipelineException: If the pipeline has a dependency cycle.
        """

        if self.handlers and not self.__dependencies_filled:
            raise PipelineException(f'Pipeline dependencies should be filled.')