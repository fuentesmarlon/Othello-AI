from rules import *
import copy

board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

player_id=1
def tree(board,player_id,valid):
    newBoard = copy.deepcopy(board)
    branches=[]
    for i in valid:
        newBoard[i]=player_id
        branches.append(newBoard)
        newBoard=copy.deepcopy(board)
    return branches

def value(board):
    countZero=0
    countNum=0
    for i in board:
        if i is 0:
            countZero+=1
        elif i not 0:
            countNum+=1
    return countZero-countNum

def minmax(node,depth,mp):
    val=0
    
    if depth==0:
        val=value(res)
    if mp:
        tree = tree(board,1,)
        bestValue=-50000
        for i in tree:
             bestValue=max(bestValue,minmax(i, depth-1, alpha, betha, False,tree))
        return bestValue
    elif not mp:
        tree=tree(board,2,)
        bestValue=50000
        for i in tree:
            bestValue = min(minmax(i, depth-1, alpha, betha, True,tree),bestValue)
        return bestValue




