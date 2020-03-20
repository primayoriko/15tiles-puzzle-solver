import math

class TileGame:
    def __init__(self, size=4, arr=[i for i in range(1,16)]):
        self.size = size
        self.elmt =  [0 for i in range(size)] * size
        for i in range(size):
            for j in range(size):
                self.elmt[i][j] = arr[i*size + j]

    def copyTile(self, other):
        self.size = other.size
        for i in range(self.size):
            for j in range(self.size):
                self.elmt[i][j] = other.elmt[i][j]


    def moveBlankDown(i, j=-1):
        if(j==-1):
            y = i//self.size
            x = i%self.size
            if(self.elmt[y][x]==0 and y != self.size-1):
                self.elmt[y][x], self.elmt[y+1][x] = self.elmt[y+1][x], self.elmt[y][x]
            else:
                print("operasi Down di ", i, " tidak valid")

    def moveBlankUp(i, j=-1):
        if(j==-1):
            y = i//self.size
            x = i%self.size
            if(self.elmt[y][x]==0 and y != 0):
                self.elmt[y][x], self.elmt[y-1][x] = self.elmt[y-1][x], self.elmt[y][x]
            else:
                print("operasi Up di ", i, " tidak valid")

    def moveBlankLeft(i, j=-1):
        if(j==-1):
            y = i//self.size
            x = i%self.size
            if(self.elmt[y][x]==0 and x != 0):
                self.elmt[y][x], self.elmt[y][x-1] = self.elmt[y][x-1], self.elmt[y][x]
            else:
                print("operasi Left di ", i, " tidak valid")

    def moveBlankRight(i, j=-1):
        if(j==-1):
            y = i//self.size
            x = i%self.size
            if(self.elmt[y][x]==0 and x != self.size):
                self.elmt[y][x], self.elmt[y][x+1] = self.elmt[y][x+1], self.elmt[y][x]
            else:
                print("operasi Right di ", i, " tidak valid")

    def countUnmatch(self, compares):
        cnt = 0
        for i in range(self.size):
            for j in range(self.size):
                cnt  = cnt + 1 if(self.elmt[i][j]!=0 and self.elmt[i][j]!=compares.elmt[i][j])\
                       else cnt
        return cnt

    def fungsiKurang(self, compares, index): #I don't know the english of it
        for i in range(self.size**2):
            if(self.elmt[i//self.size][i%self.size]==index):
                x = i%self.size
                y = i//self.size
                break

    def printElmt(self):
        for i in range(self.size):
            print(self.elmt[i])
            # for j in range(self.size):
            #     print(self.elmt[i][j]+' ')
            # print

if __name__ == "__main__":
     a = [[2,3], [51,7]]
     b = a
     a = []
     print(a)
     for i in range(2):
         print(b[i])
     #print(b)
     print(min(b))
    # pass