from typing import Generator
import itertools


def possible_final_scores() -> Generator[int, None, None]:
    """ Get all final scores include overtime.

    However, sometimes, when all 30 rounds are played, the score is 15-15,
    which means teams head into Overtime to determine the winner.
    Overtime is a best-of-six affair, with the first team to 19 winning the map.
    If the teams tie at 18-18, another Overtime begins. This repeats
    itself until one team wins the map.

    Overtime circles:
        | Circle | Start at | Draw at | Final score |
        | 1      | 15-15    | 18-18   | 19     |
        | 2      | 18-18    | 21-21   | 22     |
        | 3      | 21-21    | 24-24   | 25     |
        | 4      | 24-24    | 27-27   | 28     |
        | 5      | 27-27    | 30-30   | 31     |
        | 6      | 30-30    | 33-33   | 34     |
        and so on...
    """

    yield from itertools.count(start=16, step=3)
