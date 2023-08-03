def get_max_calories(calories: str) -> int:
    return get_top_calories(calories)


def get_top_three_calories(calories_by_elf: str) -> int:
    return get_top_calories(calories_by_elf, how_many=3)


def get_top_calories(calories_by_elf: str, how_many=1) -> int:
    # Split the list of calories by elf
    elves = calories_by_elf.split("\n\n")
    # Create a list of calories for each elf
    calories_by_elf = [[int(calorie)
                        for calorie in elf.splitlines()] for elf in elves]
    # get the total of calories for each elf
    total_calories = [sum(calories) for calories in calories_by_elf]
    # sort the array of total calories
    sorted_calories = sorted(total_calories)
    # get the top (last) n values
    return sum(sorted_calories[-how_many:])
