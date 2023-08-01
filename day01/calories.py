def get_max_calories(calories: str) -> int:
    return get_top_calories(calories)


def get_top_three_calories(calories_by_elf: str) -> int:
    return get_top_calories(calories_by_elf, how_many=3)


def get_top_calories(calories_by_elf: str, how_many=1) -> int:
    elves = calories_by_elf.split("\n\n")
    calories_by_elf = [elf.splitlines() for elf in elves]
    total_calories = [sum([int(item) for item in elf])
                      for elf in calories_by_elf]
    sorted_calories = sorted(total_calories)
    return sum(sorted_calories[how_many * -1:])
