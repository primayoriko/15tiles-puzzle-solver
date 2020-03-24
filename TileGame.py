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

    def moveBlankDown(self):
        if(self.blank_y != self.size-1):
            self.elmt[self.blank_y][self.blank_x], self.elmt[self.blank_y+1][self.blank_x] =\
                self.elmt[self.blank_y+1][self.blank_x], self.elmt[self.blank_y][self.blank_x]
            self.blank_y+=1
        else:
            print("operasi Down tidak valid")

    def moveBlankUp(self):
        if(self.blank_y != 0):
            self.elmt[self.blank_y-1][self.blank_x], self.elmt[self.blank_y][self.blank_x] =\
                self.elmt[self.blank_y][self.blank_x], self.elmt[self.blank_y-1][self.blank_x]
            self.blank_y-=1
        else:
            print("operasi Up tidak valid")

    def moveBlankLeft(self):
        if(self.blank_x != 0):
            self.elmt[self.blank_y][self.blank_x-1], self.elmt[self.blank_y][self.blank_x] =\
                self.elmt[self.blank_y][self.blank_x], self.elmt[self.blank_y][self.blank_x-1]
            self.blank_x-=1
        else:
            print("operasi Left tidak valid")

    def moveBlankRight(self):
        if(self.blank_x != self.size-1):
            self.elmt[self.blank_y][self.blank_x+1], self.elmt[self.blank_y][self.blank_x] =\
                self.elmt[self.blank_y][self.blank_x], self.elmt[self.blank_y][self.blank_x+1]
            self.blank_x+=1
        else:
            print("operasi Right tidak valid")

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