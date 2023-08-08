import rucksacks as r


def test_divide_rucksack():
    test_cases = [
        ("vJrwpWtwJgWrhcsFMMfFFhFp",
         ("vJrwpWtwJgWr", "hcsFMMfFFhFp")),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
         ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL")),
        ("PmmdzqPrVvPwwTWBwg",
         ("PmmdzqPrV", "vPwwTWBwg")),
        ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
         ("wMqvLMZHhHMvwLH", "jbvcjnnSBnvTQFn")),
        ("ttgJtRGJQctTZtZT",
         ("ttgJtRGJ", "QctTZtZT")),
        ("CrZsJsPPZsGzwwsLwLmpwMDw",
         ("CrZsJsPPZsGz", "wwsLwLmpwMDw")),
    ]

    for input, expected in test_cases:
        actual = r.divide_rucksack(input)
        print(actual)
        assert actual == expected


def test_get_item_in_both_compartments():
    test_cases = [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", "p"),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "L"),
        ("PmmdzqPrVvPwwTWBwg", "P"),
        ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "v"),
        ("ttgJtRGJQctTZtZT", "t"),
        ("CrZsJsPPZsGzwwsLwLmpwMDw", "s"),
    ]

    for input, expected in test_cases:
        print(input)
        actual = r.get_item_in_both(input)
        assert actual == expected


def test_get_priority():
    test_cases = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6),
                  ('g', 7), ('h', 8), ('i', 9), ('j', 10), ('k', 11),
                  ('l', 12), ('m', 13), ('n', 14), ('o', 15), ('p', 16),
                  ('q', 17), ('r', 18), ('s', 19), ('t', 20), ('u', 21),
                  ('v', 22), ('w', 23), ('x', 24), ('y', 25), ('z', 26),
                  ('A', 27), ('B', 28), ('C', 29), ('D', 30), ('E', 31),
                  ('F', 32), ('G', 33), ('H', 34), ('I', 35), ('J', 36),
                  ('K', 37), ('L', 38), ('M', 39), ('N', 40), ('O', 41),
                  ('P', 42), ('Q', 43), ('R', 44), ('S', 45), ('T', 46),
                  ('U', 47), ('V', 48), ('W', 49), ('X', 50), ('Y', 51),
                  ('Z', 52)]

    for input, expected in test_cases:
        actual = r.get_item_priority(input)
        assert actual == expected


def test_sum_priorities():
    input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
    expected = 157

    actual = r.sum_priorites(input)

    assert actual == expected
