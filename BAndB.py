import heapq
from TileGame import *

INF = int(1e9+7)

class Trice:
    def __init__(self,a, b, c):
        this.cost = a
        this.rootDist = b
        this.state = c

class BAndB:
    def __init__(self, root, goal):
        self.goalState = goal
        initState = Trice(root.countUnmatch(goal), 0, root) 
        self.states = [initState]
        # heapq.heapify(self.states)

    def findMinIdx(self):
        minVal, minIdx = self.states[0].cost, 0
        for i in range(1, len(this.states)):
            if minVal > self.states[i].cost:
                minVal, minIdx = elf.states[i].cost, i
        return i

    def generateChild(self, opt):
        

    def findRes(self):
        generatedState = 1
        currResult = INF
        while(len(self.states)!=0):
            currState = self.states.pop(self.findMinIdx())
            if(currResult < currState.cost):
                currLeft = TileGame()
                currRight = TileGame()
                currUp = TileGame()
                currDown = TileGame()

                if (currLeft.copyTile(currState).moveBlankLeft()):
                    generatedState+=1
                    unmatchTile = currLeft.countUnmatch(self.goalState)
                    if(unmatchTile == 0):
                        currResult = currState.rootDist + 1
                    else : 
                        leftState = Trice(unmatchTile + currState.rootDist +1, currState.rootDist +1, currLeft)
                        self.states.append(leftState)

                if (currLeft.copyTile(currState).moveBlankLeft()):
                    generatedState+=1
                    unmatchTile = currLeft.countUnmatch(self.goalState)
                    if(unmatchTile == 0):
                        currResult = currState.rootDist + 1
                    else : 
                        leftState = Trice(unmatchTile + currState.rootDist +1, currState.rootDist +1, currLeft)
                        self.states.append(leftState)

                if (currLeft.copyTile(currState).moveBlankLeft()):
                    generatedState+=1
                    unmatchTile = currLeft.countUnmatch(self.goalState)
                    if(unmatchTile == 0):
                        currResult = currState.rootDist + 1
                    else : 
                        leftState = Trice(unmatchTile + currState.rootDist +1, currState.rootDist +1, currLeft)
                        self.states.append(leftState)
                
                if (currLeft.copyTile(currState).moveBlankLeft()):
                    generatedState+=1
                    unmatchTile = currLeft.countUnmatch(self.goalState)
                    if(unmatchTile == 0):
                        currResult = currState.rootDist + 1
                    else : 
                        leftState = Trice(unmatchTile + currState.rootDist +1, currState.rootDist +1, currLeft)
                        self.states.append(leftState)

                if (currLeft.copyTile(currState).moveBlankLeft()):
                    generatedState+=1
                    unmatchTile = currLeft.countUnmatch(self.goalState)
                    if(unmatchTile == 0):
                        currResult = currState.rootDist + 1
                    else : 
                        leftState = Trice(unmatchTile + currState.rootDist +1, currState.rootDist +1, currLeft)
                        self.states.append(leftState)
        # Catat dah sampe goal belum

if __name__=='__main__':
    pass