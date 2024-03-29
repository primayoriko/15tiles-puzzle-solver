class TilePuzzle:
    def __init__(self, size=4, arr=[[0]*4 for _ in range(4)]):
        self.size = size
        self.elmt = [[0]*size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if(arr[i][j]==0):
                    self.blankX, self.blankY = j, i
                self.elmt[i][j] = arr[i][j]

    def __eq__(self, other):
        return self.size == other.size and self.elmt == other.elmt

    def copyTile(self, other):
        self.size = other.size
        for i in range(self.size):
            for j in range(self.size):
                self.elmt[i][j] = other.elmt[i][j]
        self.blankX = other.blankX
        self.blankY = other.blankY
        return self

    def moveBlankDown(self):
        if(self.blankY != self.size-1):
            self.elmt[self.blankY][self.blankX], self.elmt[self.blankY+1][self.blankX] =\
                self.elmt[self.blankY+1][self.blankX], self.elmt[self.blankY][self.blankX]
            self.blankY+=1
            return True
        return False

    def moveBlankUp(self):
        if(self.blankY != 0):
            self.elmt[self.blankY-1][self.blankX], self.elmt[self.blankY][self.blankX] =\
                self.elmt[self.blankY][self.blankX], self.elmt[self.blankY-1][self.blankX]
            self.blankY-=1
            return True
        return False

    def moveBlankLeft(self):
        if(self.blankX != 0):
            self.elmt[self.blankY][self.blankX-1], self.elmt[self.blankY][self.blankX] =\
                self.elmt[self.blankY][self.blankX], self.elmt[self.blankY][self.blankX-1]
            self.blankX-=1
            return True
        return False

    def moveBlankRight(self):
        if(self.blankX != self.size-1):
            self.elmt[self.blankY][self.blankX+1], self.elmt[self.blankY][self.blankX] =\
                self.elmt[self.blankY][self.blankX], self.elmt[self.blankY][self.blankX+1]
            self.blankX+=1
            return True
        return False

    def countUnmatch(self, compares):
        cnt = 0
        for i in range(self.size):
            for j in range(self.size):
                cnt  = cnt + 1 if(self.elmt[i][j]!=0 and self.elmt[i][j]!=compares.elmt[i][j])\
                    else cnt
        return cnt

    def fungsiKurang(self, idx=-1): 
        # Actually implementing only for 4x4 tile
        # dont know its name in english 
        self.elmt[self.blankY][self.blankX] = 16
        arrayFungsiKurang=[0 for i in range(17)]
        for i in range(self.size):
            for j in range(self.size):
                for k in range(i*self.size + j+1, self.size**2):
                    if(self.elmt[k//self.size][k%self.size]<self.elmt[i][j]):
                        # print(i, j, k//self.size, k%self.size)
                        arrayFungsiKurang[self.elmt[i][j]]+=1
                if(self.elmt[i][j] == idx):
                    self.elmt[self.blankY][self.blankX] = 0
                    return arrayFungsiKurang[idx]
        self.elmt[self.blankY][self.blankX] = 0
        return arrayFungsiKurang

    def isSolvable(self):
        arrayFungsiKurang = self.fungsiKurang()
        X = (self.blankX + self.blankY)%2
        return True if (sum(arrayFungsiKurang) + X)%2==0 else False, arrayFungsiKurang, X

    def printElmt(self):
        for i in range(self.size):
            print(self.elmt[i])
    
    def printFungsiKurangX(self):
        canSolved, arrayFungsiKurang, X = self.isSolvable()

        print("Hasil array fungsi kurang:")
        for i in range(1, len(arrayFungsiKurang)):
            print(str(i) + " : " + str(arrayFungsiKurang[i]))
        print("Jumlah : "+str(sum(arrayFungsiKurang)))

        print("Nilai X : " + str(X))
        return canSolved

if __name__=='__main__':
    arr=[]
    for i in range(4):
        arrTemp=[]
        for j in range(4):
            arrTemp.append((i*4 +j+1)%16)
        arr.append(arrTemp)

    tile = TilePuzzle(arr=arr)
    tile.printElmt()
    tile.moveBlankUp()
    tile.moveBlankLeft()
    tile.moveBlankRight()
    tile.printElmt()
    print(tile.countUnmatch(tileGoal))