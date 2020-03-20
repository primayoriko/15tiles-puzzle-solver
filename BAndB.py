import TileGame
import heapq

class Trice:
    def __init__(self,a, b, c):
        this.state = b
        this.cost = a
        this.blank = c

class BAndB:
    def __init__(self, root, blank):
        elmt_1 = Trice(0, root, blank) 
        self.states = [elmt_1]
        heapq.heapify(self.states)

    def findResult(self):
        # heapq.heapify(self.states)
        while(list(self.states))
        now = heapq.heappop(self.states)
        while(len(list(self.states))>0):
            size = now.state.size
            x = now.blank//size
            y = now.blank%size
            s1 = 
            if(now.blank != size-1){

            }


if __name__=='__main__':
    pass