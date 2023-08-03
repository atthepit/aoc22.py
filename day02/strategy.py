MOVES = {
    'A': 'r',  # r => rock
    'B': 'p',  # p => paper
    'C': 's',  # s => scissors
    'X': 'r',
    'Y': 'p',
    'Z': 's',
}

WIN_TABLE = {
    'r': 's',  # rock beats scissors
    'p': 'r',  # paper beats rock
    's': 'p',  # scissors beats paper
}

SCORES = {
    # Scores based on my pick
    'r': 1,
    'p': 2,
    's': 3,
    # Scores based on outcome
    'lose': 0,
    'draw': 3,
    'win': 6,
}


def get_score(strategy: str) -> int:
    total = 0

    for round in strategy.splitlines():
        adversary, me = round.split(' ')
        adversary_move = MOVES[adversary]
        my_move = MOVES[me]
        total += SCORES[my_move]
        if adversary_move == my_move:
            total += SCORES["draw"]
        elif WIN_TABLE[my_move] == adversary_move:
            total += SCORES['win']
        else:
            total += SCORES['lose']  # Not needed but for clarity

    return total
