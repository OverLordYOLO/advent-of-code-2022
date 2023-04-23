
def loadLines():
    lines = [0,0]
    while not (lines[-1] == "" and lines[-2] == ""):
        line = input()
        if line != "":
            line = int(line)
        lines.append(line)
    return lines[2:-1]

def parseLines(lines):
    elfs = []
    elf = []
    sum = 0
    for line in lines:
        if line == "":
            elfs.append([sum, elf])
            sum = 0
            elf = []
        else:
            elf.append(line)
            sum += line
    return elfs

def findMaxElfIndex(elfs):
    maxIndex = 0
    maxVal = 0
    for i, elf in enumerate(elfs):
        if elf[0] > maxVal:
            maxIndex = i
            maxVal = elf[0]

    return maxIndex

def find_max():
    lines = loadLines()
    elfs = parseLines(lines)
    maxElfIndex = findMaxElfIndex(elfs)
    print(f"elf n#:{maxElfIndex+1}; maxValue: {elfs[maxElfIndex][0]}")
    


if __name__ == "__main__":
    find_max()