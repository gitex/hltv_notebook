from datetime import date
from dataclasses import dataclass

from domain.base.entity import Entity

from .value_objects import Team
from .exceptions import MatchesDomainError


@dataclass
class Match(Entity):
    dt: date
    event: str
    first_team: Team
    second_team: Team

    def __post_init__(self):
        if self.first_team == self.second_team:
            raise MatchesDomainError('Team cannot play with itself.')

    @property
    def winner(self) -> Team | None:
        if self.first_team.score == self.second_team.score:
            return None

        max_score_team = max([self.first_team, self.second_team], key=lambda t: t.score.value)

        if max_score_team.score.is_final():
            return max_score_team

        return None

    @property
    def is_completed(self) -> bool:
        return bool(self.winner)
