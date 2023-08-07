SCORES_BY_MOVE = {
    'X': 1,  # rock
    'Y': 2,  # paper
    'Z': 3,  # scissors
}

SCORE_BY_ROUND_V1 = {
    'A X': 3,
    'A Y': 0,
    'A Z': 6,
    'B X': 6,
    'B Y': 3,
    'B Z': 0,
    'C X': 0,
    'C Y': 6,
    'C Z': 3,
}

SCORES_BY_OUTCOME = {
    'X': 0,  # lose
    'Y': 3,  # draw
    'Z': 6,  # win
}

SCORES_BY_ROUND_V2 = {
    'A X': 3,
    'A Y': 1,
    'A Z': 2,
    'B X': 1,
    'B Y': 2,
    'B Z': 3,
    'C X': 2,
    'C Y': 3,
    'C Z': 1,
}


def get_score(strategy: str, round_scores: dict, action_scores: dict) -> int:
    return sum([
        action_scores[round[2]] + round_scores[round]
        for round in strategy.splitlines()
    ])


def get_score_v1(strategy: str) -> int:
    return get_score(strategy, SCORE_BY_ROUND_V1, SCORES_BY_MOVE)


def get_score_v2(strategy: str) -> int:
    return get_score(strategy, SCORES_BY_ROUND_V2, SCORES_BY_OUTCOME)
