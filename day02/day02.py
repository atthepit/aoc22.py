import sys
from pathlib import Path
from strategy import get_score_v1, get_score_v2

if __name__ == "__main__":
    filename = sys.argv[1]
    reader = Path(filename)
    strategy = reader.read_text()
    print("V1 strategy gives you {0} points".format(
        get_score_v1(strategy)))
    print("V2 strategy gives you {0} points".format(
        get_score_v2(strategy)))
