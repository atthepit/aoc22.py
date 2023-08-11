def is_fully_contained(a: tuple[int, int], b: tuple[int, int]) -> bool:
    if (a[0] <= b[0] and a[1] >= b[1]):
        # a contains b
        return True

    if (b[0] <= a[0] and b[1] >= a[1]):
        # b contains a
        return True

    return False


def get_ranges(planning: str) -> list[tuple[int, int]]:
    output = []

    for line in planning.splitlines():
        a, b = line.split(',')
        start_a, end_a = a.split('-')
        range_a = (int(start_a), int(end_a))
        start_b, end_b = b.split('-')
        range_b = (int(start_b), int(end_b))
        output.append((range_a, range_b))

    return output


def get_fully_contained_sections(planning: str) -> int:
    return sum([
        int(is_fully_contained(a, b))
        for a, b in get_ranges(planning)
    ])


def is_overlapping(a: tuple[int, int], b: tuple[int, int]) -> bool:
    range_a = range(a[0], a[1] + 1)
    range_b = range(b[0], b[1] + 1)
    return len(set(range_a).intersection(range_b)) > 0


def get_overlapping_sections(planning: str) -> int:
    return sum([
        int(is_overlapping(a, b))
        for a, b in get_ranges(planning)
    ])
