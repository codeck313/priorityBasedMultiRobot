import random
import yaml
import time
import argparse
from elasticCollision import multiRobot

def reOrder(listPOI):
    indexRobot = list(range(len(listPOI)))
    random.shuffle(indexRobot)
    return indexRobot

def maxPathLength(arena, solution, poi):
    arena.clearPoints()
    arena.goalEndPoints([poi[i] for i in solution])
    finalPath, numberPoints = arena.multiRobotPlanningNinjaTechnique(maxTry = 2)
    if numberPoints == 0:
        numberPoints = float("inf")
    return finalPath, numberPoints


def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours


def getBestNeighbour(arena, neighbours, poi):
    bestPath, bestPathLength = maxPathLength(arena, neighbours[0], poi)
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentPath, currentPathLength = maxPathLength(arena, neighbour, poi)
        if currentPathLength < bestPathLength:
            bestPathLength = currentPathLength
            bestNeighbour = neighbour
            bestPath = currentPath
    return bestNeighbour, bestPathLength, bestPath


def hillClimbing(poi,dimensions,obstacles,maxTry=1,maxDiscovery=10):
    st = time.time()
    instance1 = multiRobot(dimensions,obstacles)
    for _ in range(maxTry):
        currentNeighbourOrder = reOrder(poi)
        currentPathSoution, currentPathLength = maxPathLength(
            instance1, currentNeighbourOrder, poi)
        neighbours = getNeighbours(currentNeighbourOrder)
        bestNeighbourOrder, bestNeighbourLength, bestPathSolution = getBestNeighbour(instance1, neighbours,poi)
        sameVar = 0
        while (bestNeighbourLength <= currentPathLength and sameVar < maxDiscovery and bestNeighbourLength != 0):
            currentNeighbourOrder = bestNeighbourOrder
            currentPathLength = bestNeighbourLength
            currentPathSoution = bestPathSolution
            neighbours = getNeighbours(currentNeighbourOrder)
            bestNeighbourOrder, bestNeighbourLength, bestPathSolution = getBestNeighbour(
                instance1, neighbours, poi)
            sameVar = sameVar + 1
        if currentPathLength != float('inf'):
            break
    print(time.time()-st)
    print("Result")

    return currentPathSoution, currentPathLength, currentNeighbourOrder

def unshuffleRobots(robotPath, currentOrder):
    unshuffled = [None]*len(robotPath)
    for ind,i in enumerate(currentOrder):
        unshuffled[i] = robotPath[ind]

    return(unshuffled)

def vizOutputWrapper(paths):
    outputDict = {'cost': 0}
    scheduleDict = {}
    cost = 0
    for idx,robo in enumerate(paths):
        pathList = []
        for t,path in enumerate(robo):
            pathList.append({'t': t, 'x': path[0], 'y': path[1]})
        cost = cost + t + 1
        scheduleDict['agent'+str(idx)] = pathList
    outputDict['schedule'] = scheduleDict
    outputDict['cost'] = cost

    with open('output.yaml','w') as f:
        data = yaml.safe_dump(outputDict, f)




def main():

    # Read from input file
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file containing map")

    args = parser.parse_args()


    with open(args.input) as input_file:
        try:
            param = yaml.load(input_file, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            print(exc)


    dimensions = param["map"]["dimensions"]
    obstacles = param["map"]["obstacles"]
    agents = param['agents']

    poi = []
    for agent in agents:
        startpoint = [agent['start'][0],agent['start'][1]]
        goalpoint = [agent['goal'][0],agent['goal'][1]]
        poi.append([tuple(startpoint),tuple(goalpoint)])

    out = hillClimbing(poi,dimensions,obstacles,maxTry=2, maxDiscovery=2)
    print(out)
    print("#"*10)
    unshuffled = unshuffleRobots(out[0], out[2])
    print(unshuffled)
    vizOutputWrapper(unshuffled)



if __name__ == "__main__":
    main()
