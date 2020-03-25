# import heapq
from TileGame import *

INF = int(1e9+7)

class Trice:
    def __init__(self,a, b, c):
        self.cost = a
        self.rootDist = b
        self.state = c

class BranchAndBound:
    def __init__(self, root, goal):
        self.goalState = goal
        initState = Trice(root.countUnmatch(goal), 0, root) 
        self.states = [initState]
        # heapq.heapify(self.states)

    def findMinIdx(self):
        minVal, minIdx = self.states[0].cost, 0
        for i in range(1, len(self.states)):
            if minVal > self.states[i].cost:
                minVal, minIdx = self.states[i].cost, i
        return minIdx

    def switchChildGenerator(self, obj, opt):
        switcher = {
            1 : obj.moveBlankUp, 
            2 : obj.moveBlankDown,
            3 : obj.moveBlankLeft,
            4 : obj.moveBlankRight,
        }
        func = switcher.get(opt, lambda:False)
        return func()

    def generateChild(self, parentState, opt, generatedState = 1, currCost = INF):
        child = TileGame()
        child.copyTile(parentState.state)
        cost = INF
        succ = self.switchChildGenerator(child, opt)

        if (succ):
            print(opt)
            child.printElmt()
            unmatchTile = child.countUnmatch(self.goalState)
            if(unmatchTile == 0):
                cost = parentState.rootDist + 1
            else : 
                childState = Trice(unmatchTile + parentState.rootDist + 1, parentState.rootDist + 1, child)
                self.states.append(childState)
        return generatedState + 1 if succ else generatedState , min(currCost, cost)

    def findResult(self):
        generatedState = 1
        currResult = INF
        #while(len(self.states)!=0):
        currState = self.states.pop(self.findMinIdx())
        if(currResult > currState.cost):
            generatedState, currResult = self.generateChild(currState, 1, generatedState, currResult)
            generatedState, currResult = self.generateChild(currState, 2, generatedState, currResult)
            generatedState, currResult = self.generateChild(currState, 3, generatedState, currResult)
            generatedState, currResult = self.generateChild(currState, 4, generatedState, currResult)
        return currResult, generatedState
        # Catat dah sampe goal belum

if __name__=='__main__':

    pass