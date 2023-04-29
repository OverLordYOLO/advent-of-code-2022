# two instructions addx (2 cycles), noop (1 cycle)
# addx 1 - adds 1 to register x
# signal strength = cycle number * value of X
# calculate sum of signal strengths at cycles: 20, 60, 100, 140, 180, 220

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

def calculateSumOfSignalStrenghts(instructions):
    timeStamps = [i*40+20 for i in range(6)]
    cycle = 0
    xRegister = 1
    sumOfSignalStrenghts = 0

    for i, instruction in enumerate(instructions):
        instructionType = instruction[INSTRUCTION_TYPE_INDEX]
        addNext = 0
        execTime = 1
        if instructionType == "addx":
            execTime = 2
            addNext = instruction[ADD_AMOUNT_INDEX]
        
        for j in range(execTime):
            cycle += 1
            if cycle in timeStamps:
                sumOfSignalStrenghts += xRegister * cycle
                print("------------", xRegister * cycle)
        print(xRegister, "+", addNext)
        xRegister += addNext
    return sumOfSignalStrenghts


def main():
    lines = loadLines()
    instructions = parseInstructions(lines)
    sumOfSignalStrenghts = calculateSumOfSignalStrenghts(instructions)
    print("result:",sumOfSignalStrenghts)


if __name__ == "__main__":
    main()