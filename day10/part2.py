# two instructions addx (2 cycles), noop (1 cycle)
# addx 1 - adds 1 to register x
# CRT draws pixels on screen 40 pixels wide
# one pixel per cycle
# x register is a horizontal center position of a 3pixel wide sprite
# if CRT is currently drawing on a position with the sprite, make the pixel "#", else "."

import sys
#from collections import deque

INPUT_FILE = sys.path[0] + "\\testInput.txt"
INPUT_FILE = sys.path[0] + "\\input.txt"

INSTRUCTION_TYPE_INDEX = 0
ADD_AMOUNT_INDEX = 1

INSTRUCTION_ADD = "addx"
INSTRUCTION_NOOP = "noop"

INSCTRUCTION_EXEC_TIME = {
    INSTRUCTION_ADD: 2,
    INSTRUCTION_NOOP: 1
}

def loadLines():
    lines = ""
    with open(INPUT_FILE, mode="r") as f:
        lines = [line.replace("\n", "") for line in f.readlines()]
    return lines

def parseInstructions(lines):
    moves = [line.split() for line in lines]
    for move in moves:
        if move[INSTRUCTION_TYPE_INDEX] == INSTRUCTION_ADD:
            move[ADD_AMOUNT_INDEX] = int(move[ADD_AMOUNT_INDEX])
    return moves

def createImage(instructions):
    cycle = 0
    xRegister = 1

    for i, instruction in enumerate(instructions):
        instructionType = instruction[INSTRUCTION_TYPE_INDEX]
        addNext = 0
        execTime = 1
        if instructionType == "addx":
            execTime = 2
            addNext = instruction[ADD_AMOUNT_INDEX]
        
        for j in range(execTime):
            horizontalPos = cycle % 40
            if horizontalPos == 0:
                print()
            cycle += 1
            if horizontalPos < xRegister +2 and horizontalPos > xRegister -2:
                print("#", end=" ")
            else:
                print(".", end=" ")
        xRegister += addNext


def main():
    lines = loadLines()
    instructions = parseInstructions(lines)
    createImage(instructions)


if __name__ == "__main__":
    main()