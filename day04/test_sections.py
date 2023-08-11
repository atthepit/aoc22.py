import sections


def test_fully_contains():
    test_cases = [
        (((2, 4), (6, 8)), False),
        (((2, 3), (4, 5)), False),
        (((5, 7), (7, 9)), False),
        (((2, 8), (3, 7)), True),
        (((6, 6), (4, 6)), True),
        (((2, 6), (4, 8)), False),
        (((1, 3), (1, 3)), True),
    ]

    for input, expected in test_cases:
        actual = sections.is_fully_contained(input[0], input[1])
        assert actual == expected


def test_fully_contained_sections():
    input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
    expected = 2

    actual = sections.get_fully_contained_sections(input)

    assert actual == expected


def test_overlaps():
    test_cases = [
        (((2, 4), (6, 8)), False),
        (((2, 3), (4, 5)), False),
        (((5, 7), (7, 9)), True),
        (((2, 8), (3, 7)), True),
        (((6, 6), (4, 6)), True),
        (((2, 6), (4, 8)), True),
        (((1, 3), (1, 3)), True),
    ]

    for input, expected in test_cases:
        actual = sections.is_overlapping(input[0], input[1])
        assert actual == expected


def test_overlapping_sections():
    input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
    expected = 4

    actual = sections.get_overlapping_sections(input)

    assert actual == expected
