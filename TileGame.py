import math

class TileGame:
    def __init__(self, size=4, arr=[[0]*4 for _ in range(4)]):
        self.size = size
        self.elmt = [[0]*size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if(arr[i][j]==0):
                    self.blank_x, self.blank_y = j, i
                self.elmt[i][j] = arr[i][j]

    def copyTile(self, other):
        self.size = other.size
        for i in range(self.size):
            for j in range(self.size):
                self.elmt[i][j] = other.elmt[i][j]

    def moveBlankDown(i, j=-1):
        if(j==-1):
            x,y =i%self.size, i//self.size
        else:
            x, y = j, i
        if(self.elmt[y][x]==0 and y != self.size-1):
            self.elmt[y][x], self.elmt[y+1][x] = self.elmt[y+1][x], self.elmt[y][x]
        else:
            print("operasi Down di ", i, " tidak valid")

    def moveBlankUp(i, j=-1):
        if(j==-1):
            x,y =i%self.size, i//self.size
        else:
            x, y = j, i
        if(self.elmt[y][x]==0 and y != 0):
            self.elmt[y][x], self.elmt[y-1][x] = self.elmt[y-1][x], self.elmt[y][x]
        else:
            print("operasi Up di ", i, " tidak valid")

    def moveBlankLeft(i, j=-1):
        if(j==-1):
            x,y =i%self.size, i//self.size
        else:
            x, y = j, i
        if(self.elmt[y][x]==0 and x != 0):
            self.elmt[y][x], self.elmt[y][x-1] = self.elmt[y][x-1], self.elmt[y][x]
        else:
            print("operasi Left di ", i, " tidak valid")

    def moveBlankRight(i, j=-1):
        if(j==-1):
            x,y =i%self.size, i//self.size
        else:
            x, y = j, i
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

    def fungsiKurang(self):
        sums = 0
        for i in range(4):
            for j in range(4):
                if(i == self.blank_y and j == self.blank_x):
                    # print(i, j)
                    sums += ((i+j)%2)
                else:
                    for k in range(i*self.size + j+1, 16):
                        if(self.elmt[k//self.size][k%self.size]<self.elmt[i][j]):
                            # print(i, j, k//self.size, k%self.size)
                            sums+=1 if (k//self.size != self.blank_y and k%self.size != self.blank_x) else 0
        return sums

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