import sys

inputPath = sys.path[0] + "\input.txt"
scores = {
    "A": 1,
    "B": 2,
    "C": 3
}

resultScores = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

handForResult = {
    "A": {
        "X": "C",
        "Y": "A",
        "Z": "B"
    },
    "B": {
        "X": "A",
        "Y": "B",
        "Z": "C"
    },
    "C": {
        "X": "B",
        "Y": "C",
        "Z": "A"
    }
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
        oponentHand, result = hand
        myHand = handForResult[oponentHand][result]
        score += scores[myHand] + resultScores[result]
    print(score)

if __name__ == "__main__":
    main()