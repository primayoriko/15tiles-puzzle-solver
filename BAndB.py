import heapq
from TileGame import *

INF = int(1e9+7)

class Trice:
    def __init__(self,a, b, c):
        this.state = c
        this.cost = a
        this.rootDist = b

class BAndB:
    def __init__(self, root, goal):
        self.goalState = goal
        initState = Trice(root.countUnmatch(goal), 0, root) 
        self.states = [initState]
        # heapq.heapify(self.states)

    def findRes(self):
        generatedState = 1
        currResult = INF
        while(len(self.states)!=0):
            currState = self.states.pop(self.findMinIdx())
            if(currResult<currState.cost):
                currLeft = TileGame()
                currRight = TileGame()
                currUp = TileGame()
                currDown = TileGame()

                if (currLeft.copyTile(currState).moveBlankLeft()==1):
                    generatedState+=1
                    self.states.append(currLeft)
                    if(currLeft.countUnmatch(self.goalState)==0)
                
        # Catat dah sampe goal belum

    def findMinIdx(self):
        minVal, minIdx = self.states[0].cost, 0
        for i in range(1, len(this.states)):
            if minVal > self.states[i].cost:
                minVal, minIdx = elf.states[i].cost, i
        return i

    def findResult(self):
        # heapq.heapify(self.states)
        while(list(self.states))
        now = heapq.heappop(self.states)
        while(len(list(self.states))>0):
            size = now.state.size
            x = now.blank//size
            y = now.blank%size
            s1 = 
            if(now.blank != size-1):
                return

if __name__=='__main__':
    pass