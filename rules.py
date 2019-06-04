import numpy as np
import math
import copy
from random import randint
#Helps making the board visible 


board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

checkList = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
tile=['_','X','O']
def visualizer(board):
    result = '    A  B  C  D  E  F  G  H'
    for i in range(len(board)):
        if i%8 is 0:
            result += '\n\n ' + str((math.floor(i / 8)) + 1) + ' '
        result+= ' ' + tile[board[i]] + ' '
    return result
#Turns input to list index
def ix(row,col):
    val=(row*8)+col 
    return val
#Checks if position isn't outside of borders
def margin(x,y):
    return (x>=0 and x<=7 and y>=0 and y<=7) 
#Validates move to be played 
def validateMove(board,player_id,row,col):
    enemy=0
    moves=[]
    #newBoard = copy.deepcopy(board)
    if player_id==1:
        enemy=2
    if player_id==2:
        enemy=1
    position=ix(row,col)
    if board[position] !=0 or not margin(row,col):
        return False
    for dirX,dirY in  checkList:
        x,y=row,col
        x+=dirX
        y+=dirY
        
        if (margin(x,y) and board[ix(x,y)]== enemy):
            x+=dirX
            y+=dirY
            if not margin(x,y):
                continue
            
            while board[ix(x,y)]==enemy:
                x+=dirX
                y+=dirY
                if not margin(x,y):
                    break
            if not margin(x,y):
                continue
            if board[ix(x,y)]==player_id:
                while True:
                    x-=dirX
                    y-=dirY

                    if x==row and y==col:
                        break
                    moves.append(ix(x,y))
    if len(moves) > 0:
        for i in moves:
            board[i] = player_id
        return board

    else:
        return False
