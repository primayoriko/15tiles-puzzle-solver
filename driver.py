from BranchAndBound import *

def inputTile(param, tile, filename="Puzzle_0.txt"):
    if(param==2):
        file = open(filename, "r")
    for i in range(4):
        line = input() if param==1 else file.readline()
        val = line.split()
        val = [int(val[j]) for j in range(len(val))]
        tile[i] = val
    file.close()

if __name__=='__main__':
    # param = int(input('TileGame Solver\n\nInput:\n 1. Konsol\n 2. File\n\nMasukkan tipe input: '))
    # filename = input('TileGame\n\nMasukkan nama file: ')
    param = 2
    arr=[[0]*4 for _ in range(4)]
    arrGoal=[]
    for i in range(4):
        arrTemp=[]
        for j in range(4):
            arrTemp.append((i*4 +j+1)%16)
        arrGoal.append(arrTemp)
    inputTile(param=param, tile=arr)
    tileGoal = TileGame(arr=arrGoal)
    tile = TileGame(arr=arr)
    # tile.printElmt()
    # print(tile.blank_x, tile.blank_y)
    # tile.moveBlankUp()
    # tile.moveBlankLeft()
    # tile.moveBlankRight()
    # tile.printElmt()
    #print(tile.countUnmatch(tileGoal))
    # print(tile.blankX, tile.blankY)
    Solver = BranchAndBound(tile, tileGoal)
    # print(Solver.findMinIdx())
    # if(Solver.switchChildGenerator(tile, 4)):
    #     print("succeed")
    # tile.printElmt()
    # print(Solver.states[0].cost, Solver.states[0].rootDist)
    # Solver.states[0].state.printElmt()
    minStep, totalState = Solver.findResult()
    # print(len(Solver.states))
    print(minStep, totalState)
    Solver.printSteps()

