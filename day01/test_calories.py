from calories import get_max_calories, get_top_three_calories


def test_get_max_calories():
    input = '1000\n2000\n3000\n\n4000\n\n5000\n' + \
        '6000\n\n7000\n8000\n9000\n\n10000\n'
    expected = 24000

    actual = get_max_calories(input)

    assert actual == expected


def test_get_max_calories_not_a_number():
    input = '1000\n2000\n3000\n\nhello\n\n5000\n' + \
        '6000\n\n7000\n8000\n9000\n\n10000\n'

    try:
        get_max_calories(input)
    except ValueError:
        assert True
    else:
        assert False


def test_get_max_calories_lazy_elf():
    input = '1000\n2000\n3000\n\n\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000\n'
    expected = 24000

    actual = get_max_calories(input)

    assert actual == expected


def test_get_top_three_calories():
    input = '1000\n2000\n3000\n\n4000\n\n5000\n' + \
        '6000\n\n7000\n8000\n9000\n\n10000\n'
    expected = 45000

    actual = get_top_three_calories(input)

    assert actual == expected
