# ord
# a = x-96
# if a < 0: (a * -1) - 4
import sys

debug = False
INPUT_FILE = sys.path[0] + "\input.txt"

def loadLines():
    lines = ""
    with open(INPUT_FILE, mode="r") as f:
        lines = f.readlines()
    return lines

def findMatching(lines):
    matching = []
    for line in lines:
        middleIndex = int((len(line) / 2))
        left = line[:middleIndex]
        right = line[middleIndex:]
        matching.append(set(left) & set(right))
    return matching

def calculateTotalPriority(matches):
    totalPriority = 0
    for match in matches:
        for m in match:
            calculatedPriority = ord(m)
            if (calculatedPriority > 96):
                calculatedPriority -= 96
            else:
                calculatedPriority -= 38
            totalPriority += calculatedPriority
    return totalPriority

def main():
    lines = loadLines()
    matches = findMatching(lines)
    totalPriority = calculateTotalPriority(matches)
    if debug:
        for i, match in enumerate(matches):
            print (f"{i}# matches: ", end="")
            for m in match:
                print (m, end=" ")
            print()
    print(f"Total priority: {totalPriority}")


if __name__ == "__main__":
    main()