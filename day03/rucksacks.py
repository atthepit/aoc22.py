def divide_rucksack(rucksack: str) -> tuple[str, str]:
    half = int(len(rucksack) / 2)
    return rucksack[:half], rucksack[half:]


PRIORITIES = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
    'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
    'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29,
    'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36,
    'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43,
    'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50,
    'Y': 51, 'Z': 52
}


def get_item_priority(item: str) -> int:
    if item not in PRIORITIES:
        raise ValueError(f"Item {item} doesn't have a priority")

    return PRIORITIES[item]


def get_item_in_both(rucksack: tuple[str, str]) -> str:
    left, right = rucksack
    common = set(left).intersection(set(right))

    if len(common) != 1:
        raise ValueError(f"Expected one common item but got: {str(common)}")

    return common.pop()


def sum_priorites(rucksacks: str) -> int:
    return sum([
        get_item_priority(get_item_in_both(divide_rucksack(rucksack)))
        for rucksack in rucksacks.splitlines()
    ])


def get_groups(rucksacks: list[str], n=3) -> list[list[str]]:
    groups = []
    for i in range(0, len(rucksacks), n):
        groups.append(rucksacks[i:i+n])
    return groups


def find_common(group: list[str]) -> str:
    common = set(group[0])
    for rucksack in group[1:]:
        common = common.intersection(set(rucksack))

    if len(common) != 1:
        raise ValueError(f"Expected one common item but got: {str(common)}")

    return common.pop()


def get_badges(rucksacks: list[str]) -> list[str]:
    return [find_common(group) for group in get_groups(rucksacks)]


def sum_badges_priorities(rucksacks: str) -> int:
    return sum([
        get_item_priority(badge)
        for badge in get_badges(rucksacks.splitlines())
    ])
