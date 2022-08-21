from time import sleep #sumanth comment
from random import randint
board={}
for i in range(1,101):
    board[i]=i
for i in range(1,101):
    if(i%10==0):
        print (i)
    else:
        if i <=10:
            print (str(i)+" ",end=" ")
        else:
            print (i,end=" ")


def print_board(board1):
    for i in range(1, 101):
        if (i % 10 == 0):
            print (board1[i])
        else:
            if i <= 10:
                print (str(board1[i]) + " ",end=" ")
            else:
                print (board1[i],end=" ")

def roll_die():
    return randint(1,6)

def welcome():
    sleep(1)
    print("........WELCOME TO GAME........")
    sleep(1)
    print ("SNAKE AND LADDERS")
    sleep(1)
    print_board(board)
    print ("your symbol is 'P1' and cpu symbol is 'C1'")
    sleep(1)
    print (" ")
    track=0
    user_pos=0
    cpu_pos=0
    while True:
        sleep(1)
        print( "USER TURN")
        sleep(1)
        print ("enter 't' to roll the dice")
        user_choice=input()
        if user_choice=='t':
            user=roll_die()
            sleep(1)
            print ("DIE ROLL IS " + str(user))
            if user_pos>0:
                if board[user_pos]=="DUO":
                    board[user_pos]="c1"
                else:
                    board[user_pos]=user_pos
            user_pos=user_pos+ user
            if board[user_pos]=="c1":
                board[user_pos]="DUO"
            else:
                board[user_pos]="p1"
        else:
            sleep(1)
            print ("INVALID KEY")
        sleep(1)
        print_board(board)
        sleep(1)
        print ("CPU TURN")
        sleep(1)
        cpu=roll_die()
        sleep(1)
        print ("DIE ROLL IS " + str(cpu))
        sleep(1.5)
        if cpu_pos>0:
            if board[cpu_pos]=="DUO":
                board[cpu_pos]="p1"
            else:
                board[cpu_pos]=cpu_pos
        cpu_pos = cpu_pos + cpu
        if board[cpu_pos]=="p1":
            board[cpu_pos]="DUO"
        else:
            board[cpu_pos]="c1"
        sleep(1)
        print_board(board)
        track = max(user_pos, cpu_pos)
        """if track==100:
            break
        else:"""


welcome()

