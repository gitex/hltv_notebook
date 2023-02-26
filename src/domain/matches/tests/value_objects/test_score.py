import pytest

from domain.matches.value_objects import Score


@pytest.mark.parametrize(
    'score',
    (
        Score(1),
        Score(8),
        Score(15),
        Score(18),
        Score(20),
        Score(23),
    ),
    ids=['1', '8', '15', '18', '20', '23']
)
def test_score_is_not_final(score):
    assert not score.is_final()


@pytest.mark.parametrize(
    'score',
    (
        Score(16),
        Score(19),
        Score(22),
        Score(25),
        Score(28),
        Score(31),
        Score(34),
    ),
    ids=['16', '19', '22', '25', '28', '31', '34']
)
def test_score_is_final(score):
    assert score.is_final()
