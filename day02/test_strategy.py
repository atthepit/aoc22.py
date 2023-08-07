from strategy import get_score_v1, get_score_v2


def test_startegy_score_v1():
    input = 'A Y\nB X\nC Z'
    expected = 15

    result = get_score_v1(input)

    assert result == expected


def test_startegy_score_v2():
    input = 'A Y\nB X\nC Z'
    expected = 12

    result = get_score_v2(input)

    assert result == expected
