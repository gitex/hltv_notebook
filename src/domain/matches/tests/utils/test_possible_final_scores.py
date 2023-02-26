import itertools

from domain.matches.utils import possible_final_scores


def test_first_eight_possible_scores():
    """ Test possible scores which finish game.

    You can check overtime description in docstring of `possible_final_scores`
    """
    expected = [16, 19, 22, 25, 28, 31, 34]
    gotten = list(itertools.islice(possible_final_scores(), len(expected)))
    assert gotten == expected


