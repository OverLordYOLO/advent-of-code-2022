# group of 3
# every elf has a group badge
# badge is the only common item

# find the common item between all three elves

import sys

debug = False
INPUT_FILE = sys.path[0] + "\input.txt"

def loadLines():
    lines = ""
    with open(INPUT_FILE, mode="r") as f:
        lines = [line.rstrip() for line in f.readlines()]
    return lines

def findMatching(lines):
    matching = []
    print(len(lines))
    for i in range(0, len(lines), 3):
        matching.append(set(lines[i]) & set(lines[i+1]) & set(lines[i+2]))
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