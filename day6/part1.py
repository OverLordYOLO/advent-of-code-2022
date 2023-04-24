import sys

INPUT_FILE = sys.path[0] + "\\input.txt"

def loadLines():
    lines = ""
    with open(INPUT_FILE, mode="r") as f:
        lines = [line.replace("\n", "") for line in f.readlines()]
    return lines

def findMarkerIndex(text):
    for i in range(4, len(text)):
        freq = {}
        for j in range(i-4, i):
            if text[j] in freq:
                freq[text[j]] += 1
            else:
                freq[text[j]] = 1
        isUnique = len([val for val in freq.values() if val != 1]) == 0
        if (isUnique):
            return i


def main():
    lines = loadLines()
    for line in lines:
        markerIndex = findMarkerIndex(line)
        print("first marker after character:", markerIndex)


if __name__ == "__main__":
    main()