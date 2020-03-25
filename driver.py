import sys
from BranchAndBound import *

def inputTile(tile, param=1, filename="Puzzle.txt"):
    if(param==1):
        file = open(filename, "r")
    for i in range(4):
        line = input() if param==2 else file.readline()
        val = line.split()
        val = [int(val[j]) for j in range(len(val))]
        tile[i] = val
    file.close()

if __name__=='__main__':
    # Defining array goal
    arrGoal=[]
    for i in range(4):
        arrTemp=[]
        for j in range(4):
            arrTemp.append((i*4 +j+1)%16)
        arrGoal.append(arrTemp)
    tileGoal = TilePuzzle(arr=arrGoal)
    
    # Defining start array
    # filename = input('15-Tile Puzzle Solver\n\nMasukkan nama file: ')
    filename = str(sys.argv[1])
    print(filename)
    arr=[[0]*4 for _ in range(4)]
    inputTile(tile=arr, filename=filename)
    tile = TilePuzzle(arr=arr)

    # Counting fungsi kurang
    print("Array hasil input file "+filename+":")
    tile.printElmt()
    print("")
    canSolved = tile.printFungsiKurangX()

    if(not canSolved):
        print("\nTile tidak bisa diselesaikan!\nJumlah Fungsi kurang + X ganjil!")
    else:
        print("\nTile bisa diselesaikan!\nTotal Fungsi kurang + X genap!")
        Solver = BranchAndBound(tile, tileGoal)
        minStep, totalState = Solver.findResult()
        # print(len(Solver.states))
        print("")
        print("Banyak Step dibutuhkan : " + str(minStep))
        print("Banyak State di generate : " + str(totalState))
        print("")
        Solver.printSteps()

