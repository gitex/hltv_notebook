from dataclasses import dataclass
from typing import Protocol, TypeVar, Type


In = TypeVar('In')    # A type variable used to indicate the input data type.
Out = TypeVar('Out')  # A type variable used to indicate the output data type.


class IFactory(Protocol):
    """ Defines the interface for a factory that takes an input of type Input
    and returns an output of type Output.
    """

    def __call__(self, data: In) -> Out | None:
        """ This method is called when the factory is invoked with an input data. """
        ...


@dataclass
class CompositeFactory(IFactory):
    """ Aggregates multiple IFactory objects and applies them to the input data sequentially.

    If any of the factories in the composite return None, the composite factory returns None as well.
    """

    factories: list[Type[IFactory]]

    def __call__(self, data: In) -> Out | None:
        """ Applies the factories to the input data sequentially. """

        for factory_class in self.factories:
            factory = factory_class()
            data = factory(data)

            if data is None:
                return None

        return data
