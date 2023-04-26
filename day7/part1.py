import sys
from collections import deque

#INPUT_FILE = sys.path[0] + "\\testInput.txt"
INPUT_FILE = sys.path[0] + "\\input.txt"
CMD_LINE_TYPE = "CMD"
OUT_LINE_TYPE = "OUT"

def loadLines():
    lines = ""
    with open(INPUT_FILE, mode="r") as f:
        lines = [line.replace("\n", "") for line in f.readlines()]
    return lines

def parseLines(lines):
        # COMMANDS:
        # $ cd
        #   - /
        #   - ..
        #   - [dirname]
        # $ ls
        # OUTPUTS:
        # dir [dirname]
        # [filesize] [filename]
    parsed = []
    for line in lines:
        lineType = ""
        if (line.startswith('$')):
            lineType = CMD_LINE_TYPE
        else:
            lineType = OUT_LINE_TYPE
        a = line.rstrip().split(" ")[-2:]
        firstPart, secondPart = line.rstrip().split(" ")[-2:]
        parsed.append([lineType, firstPart, secondPart])
    return parsed

def changeDir(currentDir, changeTo):
    match changeTo:
        case "/":
            currentDir = ["/"]
        case "..":
            if len(currentDir) > 1:
                currentDir.pop()
        case _:
            currentDir.append(changeTo)

def createPath(currentDir):
    path = ["", ""]
    if len(currentDir) > 1:
        path = [""] + currentDir[1:]
    return "/".join(path)

def addToSystemMap(systemMap, currentDir, firstParam, name):
    match firstParam:
        case "dir":
            systemMap["/".join(currentDir + [name])[1:]] = {"files": [], "dirSize": 0}
        case _:
            fileSize = int(firstParam)
            path = createPath(currentDir)
            systemMap[path]["files"].append([name, fileSize])
            
            for i in range(len(currentDir)-1, -1, -1):
                systemMap[path]["dirSize"] += fileSize
                path = createPath(currentDir[:i])


def mapDirectories(parsedLines):
    currentDir = ["/"]
    systemMap = {"/": {"files": [], "dirSize": 0}}
    commandTypeIndex = 0
    firstParamIndex = 1
    secondParamIndex = 2
    for line in parsedLines:
        match line[commandTypeIndex]:
            case "CMD":
                if line[firstParamIndex] == "cd":
                    changeDir(currentDir, line[secondParamIndex])
            case "OUT":
                addToSystemMap(systemMap, currentDir, line[firstParamIndex], line[secondParamIndex])
            case _:
                raise f"Unexpected case!! : {line[commandTypeIndex]}"
    return systemMap

def sumDirSizes(mapped, maxSize):
    sum = 0
    for dirName, val in mapped.items():
        if val["dirSize"] <= maxSize:
            sum += val["dirSize"]
    return sum

def main():
    lines = loadLines()
    parsedLines = parseLines(lines)
    maxSize = 100000
    mapped = mapDirectories(parsedLines)
    sum = sumDirSizes(mapped, maxSize)
    print(sum)


if __name__ == "__main__":
    main()