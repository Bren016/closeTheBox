def isEqual(choices, roll) -> bool:
    total = 0
    for num in choices:
        total += num.getValue()

    return total == roll


def removeFromBoard(board, choices):
    for num in choices:
        board.remove(num.getValue())


def possibleSolution(board, roll):
    return rollInBoard(board, roll) or cansum(board, roll) or (cansum3(board, roll))


def rollInBoard(board, roll):
    for num in board:
        if num == roll:
            return True
    return False


def cansum(board, roll):
    for i in board:
        for j in board:
            if i != j and i + j == roll:
                return True
    return False


def cansum3(board, roll):
    for i in board:
        for j in board:
            for k in board:
                if i != j and i != k and j != k and i + j + k == roll:
                    return True
    return False
