from strategy import get_score


def test_startegy_score():
    input = 'A Y\nB X\nC Z'
    expected = 15

    result = get_score(input)

    assert result == expected
