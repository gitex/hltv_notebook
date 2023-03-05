from dataclasses import dataclass
from typing import Optional

from domain.base.value_object import ValueObject

from .stubs import TeamName
from .utils import possible_final_scores


@dataclass(frozen=True)
class Score(ValueObject):
    """ Match one side score. """

    value: int

    def __post_init__(self):
        if not isinstance(self.value, int):
            raise TypeError('Score should be integer type.')

        if self.value < 0:
            raise ValueError('Score should be positive.')

    def is_final(self) -> bool:
        """ Score is final and game can be finished here.

        We should be accurate with this because 16-19 has two final scores.
        """
        for possible_score in possible_final_scores():
            if self.value == possible_score:
                return True

            if possible_score > self.value:
                break

        return False

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f'Should be {self.__class__} type')

        return hash(self) == hash(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.value)


@dataclass(frozen=True)
class Team(ValueObject):
    name: TeamName
    score: Score

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, Team):
            raise TypeError(f'Should be {self.__class__} type.')

        return hash(self) == hash(other)
