# input -> movements of head
# tail moves towards head, if head further than 1 block (diagonal / horizontal / vertical)
# if head not in the same row and col as tail, tail moves diagnoal

import sys
#from collections import deque

INPUT_FILE = sys.path[0] + "\\testInput.txt"
INPUT_FILE = sys.path[0] + "\\input.txt"

MOVE_UP = "U"
MOVE_DOWN = "D"
MOVE_LEFT = "L"
MOVE_RIGHT = "R"
MOVE_UP_LEFT = "UL"
MOVE_UP_RIGHT = "UR"
MOVE_DOWN_LEFT = "DL"
MOVE_DOWN_RIGHT = "DR"
MOVE_NONE = "N"

MOVEMENT_AMOUNT = {
    MOVE_UP: {"y": 1, "x": 0},
    MOVE_DOWN: {"y": -1, "x": 0},
    MOVE_LEFT: {"y": 0, "x": -1},
    MOVE_RIGHT: {"y": 0, "x": 1},
    MOVE_UP_LEFT: {"y": 1, "x": -1},
    MOVE_UP_RIGHT: {"y": 1, "x": 1},
    MOVE_DOWN_LEFT: {"y": -1, "x": -1},
    MOVE_DOWN_RIGHT: {"y": -1, "x": 1},
    MOVE_NONE: {"y": 0, "x": 0},
}

MOVEMENT_DIRECTION = [
    [MOVE_UP_LEFT, MOVE_UP_LEFT, MOVE_UP, MOVE_UP_RIGHT, MOVE_UP_RIGHT],
    [MOVE_UP_LEFT, MOVE_NONE, MOVE_NONE, MOVE_NONE, MOVE_UP_RIGHT],
    [MOVE_LEFT, MOVE_NONE, MOVE_NONE, MOVE_NONE, MOVE_RIGHT],
    [MOVE_DOWN_LEFT, MOVE_NONE, MOVE_NONE, MOVE_NONE, MOVE_DOWN_RIGHT],
    [MOVE_DOWN_LEFT, MOVE_DOWN_LEFT, MOVE_DOWN, MOVE_DOWN_RIGHT, MOVE_DOWN_RIGHT]
]
STEP_DIRECTION_INDEX = 0
STEP_COUNT_INDEX = 1

def loadLines():
    lines = ""
    with open(INPUT_FILE, mode="r") as f:
        lines = [line.replace("\n", "") for line in f.readlines()]
    return lines

def parseMoves(lines):
    moves = [line.split() for line in lines]
    for move in moves:
        move[STEP_COUNT_INDEX] = int(move[STEP_COUNT_INDEX])
    return moves

def calculateTailMovement(i, headX, headY, tailX, tailY):
    dX = headX - tailX
    dY = tailY - headY
    md = MOVEMENT_DIRECTION[dY+2][dX+2]
    # print(i, md)
    return md

def showPositions(headX, headY, knots):
    lowestX = min(headX, 0)
    lowestY = min(headY, 0)
    highestX = max(headX, 0)
    highestY = max(headY, 0)
    for knot in knots:
        lowestX = min(knot["x"], lowestX)
        lowestY = min(knot["y"], lowestY)
        highestX = max(knot["x"], highestX)
        highestY = max(knot["y"], highestY)

    field = [['.' for j in range(max(highestX-lowestX+2, 20))] for i in range(max(highestY-lowestY+2, 20))]
    for knot in knots:
        field[knot["y"]-lowestY][knot["x"]-lowestX] = knot["i"]
    field[headY-lowestY][headX-lowestX] = 'H'
    field.reverse()
    # print(" "*15, "________")
    for line in field:
        print(" "*10, end="")
        for point in line:
            print(point, end="")
        print()
    # print(" "*15, "____")

def calculateTailPositions(moves):
    headX, headY = 0, 0
    tailX, tailY = 0, 0
    NUMBER_OF_KNOTS = 9
    last_knot_index = NUMBER_OF_KNOTS - 1
    knots = [{"i": i, "x": 0, "y": 0} for i in range(NUMBER_OF_KNOTS)]
    visitedPositions = {}
    visitedPositions[f"{tailX}:{tailY}"] = [tailY, tailX] # add starting position

    for move in moves:
        for i in range(move[STEP_COUNT_INDEX]):
            headX += MOVEMENT_AMOUNT[move[STEP_DIRECTION_INDEX]]["x"]
            headY += MOVEMENT_AMOUNT[move[STEP_DIRECTION_INDEX]]["y"]
            previousKnot = {"x": headX, "y": headY}
            # print("H", move[STEP_DIRECTION_INDEX])
            for j in range(0, NUMBER_OF_KNOTS):
                currentKnot = knots[j]
                tailStepDirection = calculateTailMovement(currentKnot["i"],
                    previousKnot["x"], previousKnot["y"], currentKnot["x"], currentKnot["y"]
                    )
                currentKnot["x"] += MOVEMENT_AMOUNT[tailStepDirection]["x"]
                currentKnot["y"] += MOVEMENT_AMOUNT[tailStepDirection]["y"]
                if j == last_knot_index and tailStepDirection != MOVE_NONE:
                    visitedPositions[f"{currentKnot['y']}:{currentKnot['x']}"] = [currentKnot["y"], currentKnot["x"]]
                previousKnot = currentKnot
            # showPositions(headX, headY, knots)
    return visitedPositions

def showVisitedPositions(visitedPositions):
    field = [['.' for j in range(6)] for i in range(5)]
    for visitedPos in visitedPositions.values():
        field[visitedPos[0]][visitedPos[1]] = '#'
    field.reverse()
    for line in field:
        for point in line:
            print(point, end="")
        print()

def main():
    lines = loadLines()
    moves = parseMoves(lines)
    visitedPositions = calculateTailPositions(moves)
    #showVisitedPositions(visitedPositions)
    result = len(visitedPositions)
    print("number of visited positions:", result)


if __name__ == "__main__":
    main()

# 13277 - too high
# 12600 - too high