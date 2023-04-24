# clear trees
# sections with UID
# each elf has assigned range or UIDs
# elfs are in pairs

# find pairs in which one elf is fully contained by his partner


import sys

debug = False
INPUT_FILE = sys.path[0] + "\input.txt"


def loadLines():
    lines = ""
    with open(INPUT_FILE, mode="r") as f:
        lines = [line.rstrip() for line in f.readlines()]
    return lines

def parseLines(lines):
    pairs = []
    for line in lines:
        left, right = line.split(",")
        leftBeginning, leftEnd = left.split("-")
        rightBeginning, rightEnd = right.split("-")
        pairs.append([int(leftBeginning), int(leftEnd), int(rightBeginning), int(rightEnd)])
    return pairs

def calculateFullyContained(pairs):
    count = 0
    for pair in pairs:
        #if set(range(pair[0], pair[1])).issubset(range(pair[2], pair[3]))
        if (pair[0] <= pair[2] and pair[1] >= pair[3]) or (pair[2] <= pair[0] and pair[3] >= pair[1]):
            count += 1
    return count

def main():
    lines = loadLines()
    pairs = parseLines(lines)
    numberOfFullyContained = calculateFullyContained(pairs)
    print("fully contained: ", numberOfFullyContained)


if __name__ == "__main__":
    main()