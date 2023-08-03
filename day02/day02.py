import sys
from pathlib import Path
from strategy import get_score

if __name__ == "__main__":
    filename = sys.argv[1]
    reader = Path(filename)
    strategy = reader.read_text()
    print("This strategy gives you {0} points".format(
        get_score(strategy)))
