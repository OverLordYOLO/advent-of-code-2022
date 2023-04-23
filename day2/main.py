import sys

inputPath = sys.path[0] + "\input.txt"
scores = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
result = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3
    },
}

def loadLines():
    lines = ""
    with open(inputPath, mode="r") as f:
        lines = f.readlines()
    return lines

def parseInstructions(lines):
    moves = []
    for line in lines:
        moves.append(line.replace("\n", "").split(" "))
    return moves


def main():
    lines = loadLines()
    parsed = parseInstructions(lines)
    score = 0
    for hand in parsed:
        oponentHand, myHand = hand
        score += scores[myHand] + result[oponentHand][myHand]
    print(score)

if __name__ == "__main__":
    main()