import sys
#from collections import deque

# INPUT_FILE = sys.path[0] + "\\testInput.txt"
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
        peripheral = rowIndex == outerLoopFrom or rowIndex == (outerLoopTo - stepOuter)
        tallest = -1
        for colIndex in range(innerLoopFrom, innerLoopTo, stepInner):
            if peripheral or colIndex == innerLoopFrom or colIndex == (innerLoopTo - stepInner):
                tallest = trees[rowIndex][colIndex]
                continue
            currentHeight = trees[rowIndex][colIndex]
            if currentHeight > tallest:
                tallest = currentHeight
                key = f"{rowIndex}:{colIndex}"
                if not key in visibleTrees:
                    visibleTrees[key] = {"y": rowIndex, "x": colIndex}

def loopCol(visibleTrees, trees, outerLoopFrom, outerLoopTo, innerLoopFrom, innerLoopTo):
    stepOuter = int(outerLoopFrom < outerLoopTo) * 2 - 1
    stepInner = int(innerLoopFrom < innerLoopTo) * 2 - 1
    for colIndex in range(outerLoopFrom, outerLoopTo, stepOuter):
        peripheral = colIndex == outerLoopFrom or colIndex == (outerLoopTo - stepOuter)
        tallest = -1
        for rowIndex in range(innerLoopFrom, innerLoopTo, stepInner):
            if peripheral or rowIndex == innerLoopFrom or rowIndex == (innerLoopTo - stepInner):
                tallest = trees[rowIndex][colIndex]
                continue
            currentHeight = trees[rowIndex][colIndex]
            if currentHeight > tallest:
                tallest = currentHeight
                key = f"{rowIndex}:{colIndex}"
                if not key in visibleTrees:
                    visibleTrees[key] = {"y": rowIndex, "x": colIndex}

def findVisibleTrees(trees):
    height = len(trees)
    width = len(trees[0]) 
    # numberOfPerimeterTrees = width * 2 + height * 2 - 4
    
    visibleTrees = {}
    loopCol(visibleTrees, trees, 0, width, 0, height)
    loopCol(visibleTrees, trees, 0, width, height-1, -1)
    loopRow(visibleTrees, trees, 0, height, 0, width)
    loopRow(visibleTrees, trees, 0, height, width-1, -1)
    
    return visibleTrees

def findBiggestView(trees, visibleTrees):
    biggest = 0
    height = len(trees)
    width = len(trees[0]) 
    for visibleTree in visibleTrees.values():
        top = visibleTree["y"]
        bottom = height -1 - visibleTree["y"]
        right = width -1 - visibleTree["x"]
        left = visibleTree["x"]
        for i, x in enumerate(range(visibleTree["x"]-1, -1, -1)):
            if trees[visibleTree["y"]][x] >= trees[visibleTree["y"]][visibleTree["x"]]:
                left = i + 1
                break
        for i, x in enumerate(range(visibleTree["x"]+1, width, 1)):
            if trees[visibleTree["y"]][x] >= trees[visibleTree["y"]][visibleTree["x"]]:
                right = i + 1
                break
        for i, y in enumerate(range(visibleTree["y"]-1, -1, -1)):
            if trees[y][visibleTree["x"]] >= trees[visibleTree["y"]][visibleTree["x"]]:
                top = i + 1
                break
        for i, y in enumerate(range(visibleTree["y"]+1, height, 1)):
            if trees[y][visibleTree["x"]] >= trees[visibleTree["y"]][visibleTree["x"]]:
                bottom = i + 1
                break
        visibleArea = top * right * bottom * left
        print("y:", visibleTree["y"], "x:", visibleTree["x"], end=" => ")
        print(top, left, right, bottom, sep=" * ", end=" ")
        print("=", visibleArea)
        if visibleArea > biggest:
            biggest = visibleArea
    return biggest

def main():
    lines = loadLines()
    trees = parseLines(lines)
    visibleTrees = findVisibleTrees(trees)
    biggestView = findBiggestView(trees, visibleTrees)
    print(f"biggest view:", biggestView)
    #print(f"testinput result.. Which is:", biggestView == 8)


if __name__ == "__main__":
    main()


# 570648 - too high