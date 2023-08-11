import sys
from pathlib import Path
import sections


if __name__ == "__main__":
    filename = sys.argv[1]
    reader = Path(filename)
    planning = reader.read_text()

    result1 = sections.get_fully_contained_sections(planning)
    print(f"There are {result1} fully contained sections")

    result2 = sections.get_overlapping_sections(planning)
    print(f"There are {result2} overlapping sections")
