import sys

INPUT_FILE = sys.path[0] + "\input.txt"

def loadLines():
    lines = ""
    with open(INPUT_FILE, mode="r") as f:
        lines = [line.replace("\n", "") for line in f.readlines()]
    return lines

def parsePiles(lines):
    numberOfPiles = int((len(lines[0])+1) / 4)
    piles = [[] for i in range(numberOfPiles)]
    instructionStartIndex = 0
    for i, line in enumerate(lines):
        if line[1] == "1":
            instructionStartIndex = i + 2
            break;
        for i in range(numberOfPiles):
            crateLetter = line[i*4+1]
            if crateLetter != " ":
                piles[i].append(crateLetter)
    for pile in piles:
        pile.reverse()

    movementInstructions = []
    for line in lines[instructionStartIndex:]:
        _, moveAmount, _, fromPile, _, toPile = line.split(" ")
        movementInstructions.append(
            [int(fromPile)-1, int(toPile)-1, int(moveAmount)])
    
    return [ piles, movementInstructions ]

def applyMovements(piles, movementInstructions):
    # print("applying moves:")
    for move in movementInstructions:
        fromPile, toPile, moveAmount = move
        piles[toPile].extend([piles[fromPile].pop() for _ in range(moveAmount)])
        # print(piles)
    # print("end")


def main():
    lines = loadLines()
    piles, movementInstructions = parsePiles(lines)
    #print(piles)
    applyMovements(piles, movementInstructions)
    #print(piles)

    print("top crates are: ")
    print("".join([pile[-1] for pile in piles]))

if __name__ == "__main__":
    main()