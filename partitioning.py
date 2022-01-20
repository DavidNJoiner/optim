def simulateDoors(x, y, minimumDoorWidth, even):

        def findWidth(wallWidth):
            doorWidth = wallWidth
            div = 2
            while (doorWidth > minimumDoorWidth):
                div += 2 if even else div + 1
                doorWidth = int(wallWidth/div)
            return doorWidth

        xDoorWidth = findWidth(x)
        yDoorWidth = findWidth(y)
        ratio = xDoorWidth/yDoorWidth

        return [[int(x/xDoorWidth), xDoorWidth],[int(y/yDoorWidth), yDoorWidth], ratio]

         
def search(x, y, minWidthInterval, even = True):
    
    optimSolution = []
    minWidthIntervalList = makeInterval(minWidthInterval[0], minWidthInterval[-1], 100)
    
    for width in minWidthIntervalList:
        solution = simulateDoors(x, y, width, even)
        optimSolution = getBestRatio(solution, optimSolution)
    return optimSolution

def getBestRatio(solution, currentOptimSolution):

    if not currentOptimSolution or solution[2] - 1 < currentOptimSolution[2] - 1:
        return solution
    else:
        return currentOptimSolution
        pass    

def makeInterval(start, end, step):

    possibleWidth = []
    index = start

    while index < end+step:
        possibleWidth.append(i)
        index += step

    return possibleWidth



    

