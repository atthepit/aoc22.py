import sys
from pathlib import Path
from rucksacks import sum_priorites, sum_badges_priorities


if __name__ == "__main__":
    filename = sys.argv[1]
    reader = Path(filename)
    rucksacks = reader.read_text()
    print("The priority of repeating items is {0}".format(
        sum_priorites(rucksacks)))
    print("The priority of badges is {0}".format(
        sum_badges_priorities(rucksacks)))
