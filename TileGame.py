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
        return self

    def moveBlankDown(self):
        if(self.blank_y != self.size-1):
            self.elmt[self.blank_y][self.blank_x], self.elmt[self.blank_y+1][self.blank_x] =\
                self.elmt[self.blank_y+1][self.blank_x], self.elmt[self.blank_y][self.blank_x]
            self.blank_y+=1
            return 1
        return 0
        # else:
        #     print("operasi Down tidak valid")

    def moveBlankUp(self):
        if(self.blank_y != 0):
            self.elmt[self.blank_y-1][self.blank_x], self.elmt[self.blank_y][self.blank_x] =\
                self.elmt[self.blank_y][self.blank_x], self.elmt[self.blank_y-1][self.blank_x]
            self.blank_y-=1
            return 1
        return 0
        # else:
        #     print("operasi Up tidak valid")

    def moveBlankLeft(self):
        if(self.blank_x != 0):
            self.elmt[self.blank_y][self.blank_x-1], self.elmt[self.blank_y][self.blank_x] =\
                self.elmt[self.blank_y][self.blank_x], self.elmt[self.blank_y][self.blank_x-1]
            self.blank_x-=1
            return 1
        return 0
        # else:
        #     print("operasi Left tidak valid")

    def moveBlankRight(self):
        if(self.blank_x != self.size-1):
            self.elmt[self.blank_y][self.blank_x+1], self.elmt[self.blank_y][self.blank_x] =\
                self.elmt[self.blank_y][self.blank_x], self.elmt[self.blank_y][self.blank_x+1]
            self.blank_x+=1
            return 1
        return 0
        # else:
        #     print("operasi Right tidak valid")

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
    if(param==2):
        file = open(filename, "r")
    for i in range(4):
        line = input() if param==1 else file.readline()
        val = line.split()
        val = [int(val[j]) for j in range(len(val))]
        tile[i] = val
    file.close()

if __name__=='__main__':
    arr=[]
    for i in range(4):
        arrTemp=[]
        for j in range(4):
            arrTemp.append((i*4 +j+1)%16)
        arr.append(arrTemp)

    tile = TileGame(arr=arr)
    tile.printElmt()
    tile.moveBlankUp()
    tile.moveBlankLeft()
    tile.moveBlankRight()
    tile.printElmt()
    print(tile.countUnmatch(tileGoal))