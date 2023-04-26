import sys
#from collections import deque

#INPUT_FILE = sys.path[0] + "\\testInput.txt"
INPUT_FILE = sys.path[0] + "\\input.txt"

def loadLines():
    lines = ""
    with open(INPUT_FILE, mode="r") as f:
        lines = [line.replace("\n", "") for line in f.readlines()]
    return lines

def parseLines(lines):
    return [[int(tree) for tree in line] for line in lines]

def loopRow(visibleTrees, trees, outerLoopFrom, outerLoopTo, innerLoopFrom, innerLoopTo):
    stepOuter = int(outerLoopFrom < outerLoopTo) * 2 - 1
    stepInner = int(innerLoopFrom < innerLoopTo) * 2 - 1
    for rowIndex in range(outerLoopFrom, outerLoopTo, stepOuter):
        tallest = -1
        for colIndex in range(innerLoopFrom, innerLoopTo, stepInner):
            currentHeight = trees[rowIndex][colIndex]
            if currentHeight > tallest:
                tallest = currentHeight
                visibleTrees[rowIndex][colIndex] = True

def loopCol(visibleTrees, trees, outerLoopFrom, outerLoopTo, innerLoopFrom, innerLoopTo):
    stepOuter = int(outerLoopFrom < outerLoopTo) * 2 - 1
    stepInner = int(innerLoopFrom < innerLoopTo) * 2 - 1
    for colIndex in range(outerLoopFrom, outerLoopTo, stepOuter):
        tallest = -1
        for rowIndex in range(innerLoopFrom, innerLoopTo, stepInner):
            currentHeight = trees[rowIndex][colIndex]
            if currentHeight > tallest:
                tallest = currentHeight
                visibleTrees[rowIndex][colIndex] = True

def countVisibleTrees(trees):
    height = len(trees)
    width = len(trees[0]) 
    # numberOfPerimeterTrees = width * 2 + height * 2 - 4
    
    visibleTrees = [[False for col in range(width)] for row in range(height)]
    loopCol(visibleTrees, trees, 0, width, 0, height)
    loopCol(visibleTrees, trees, 0, width, height-1, -1)
    loopRow(visibleTrees, trees, 0, height, 0, width)
    loopRow(visibleTrees, trees, 0, height, width-1, -1)
    
    numberOfVisibleTrees = 0
    for i in range(height):
        for j in range(width):
            numberOfVisibleTrees += int(visibleTrees[i][j])
    return numberOfVisibleTrees

def main():
    lines = loadLines()
    trees = parseLines(lines)
    numberOfVisibleTrees = countVisibleTrees(trees)
    print(f"visible trees:", numberOfVisibleTrees)
    #print(f"testinput result.. Which is:", numberOfVisibleTrees == 21)


if __name__ == "__main__":
    main()


# 1791 - too low