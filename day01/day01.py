import sys
from pathlib import Path
from calories import get_max_calories, get_top_three_calories

if __name__ == "__main__":
    filename = sys.argv[1]
    reader = Path(filename)
    calories = reader.read_text()
    print("The elf carrying the most calories is carying {0} calories".format(
        get_max_calories(calories)))
    print("The top three elves carry {0} calories".format(
        get_top_three_calories(calories)))
