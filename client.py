import socketio
from random import randint,choice
import math
from rules import *
#main socket
sio = socketio.Client()
userName=input("add username:  ")
#tournamentId=int(input("tournament id:  "))
tournamentId=input("tournament id:  ")

def human_board(board):
    tileRep = ['_', 'X', 'O']
    N = 8
    result = '    A  B  C  D  E  F  G  H'
    for i in range(len(board)):
        if i % N == 0:
            result += '\n\n ' + str(int(math.floor(i / N)) + 1) + ' '
        result += ' ' + tileRep[board[i]] + ' '
    return result

def validateHumanPosition(position,data):
    board=data['board']
    #print (position)
    #index='abcdefgh'.index(position[1])
    #val=(int(position[0])-1)*8+index 
    #print(board[val],len(board))
    return board[position]==0


def play(board,player_id):
    #alph=['a','b','d','f','g','h']
    #move += str(randint(0,63))
    #move += choice(alph)
#uses validateMove to get all posible valid choices 
    valid=[]
    for i in range(len(board)):
        x = math.floor(i/8)
        y = i % 8
        check =validateMove(board,player_id,x,y)
        if not check:
            continue
        valid.append(i)
    action=valid[randint(0,len(valid)-1)]
    #if len(action)<=0:
    #    return  
    #else:
    return action
    
    
    """
    move=""
    alph=['a','b','d','f','g','h']
    move += str(randint(1,8))
    move += choice(alph)
    print(move)
    return move """


@sio.on('connect')
def on_connect():
    print("Hello Freak Bitches")
    sio.emit('signin',{
        "user_name":userName,
        "tournament_id":tournamentId,
        "user_role":"player"
    })

@sio.on('ready')
def on_ready(data):
    #movement = randint(0,63)
    
   # while not validateHumanPosition(movement,data):
    #movement=randint(0,63)
    #print("movement",movement)
    #print("board",data['board'])
    #print("player",data['player_turn_id'])
    print(visualizer(data['board']))
    sio.emit('play',
    {
        "player_turn_id":data['player_turn_id'],
        "tournament_id":tournamentId,
        "game_id":data['game_id'],
        "movement":play(data['board'],data['player_turn_id'])
    })
@sio.on('finish')
def on_finish(data):
    print("game has finished Cuz "+ str(data['game_id']))
    sio.emit('player_ready',{
        "tournament_id":tournamentId,
        "game_id":data['game_id'],
        "player_turn_id":data['player_turn_id']
    })

sio.connect("http://192.168.1.148:4000")