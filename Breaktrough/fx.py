
from color import *

# i've choice to call my variables ll for n (because it's len ligne ) and lc for p (because it's len collumn )
# it's easier
def newBoard(ll,lc):
    tbl = [['.']*lc for i in range(ll)]

    for t in range(0,lc):
        tbl[0][t] = 'x'
        tbl[1][t] = 'x'

        tbl[-1][t] = 'o'
        tbl[-2][t] = 'o'

    return tbl

def display(table,ll,lc):
    # lc = len(table[0])
    # ll = len(table)
    test = '   '
    for v in range(1,lc+1):
        if v == 9:
            test += str(v)+' '
        elif v <10:
            test += str(v)+'  '
        else:
            test += str(v)+' '
    red(test)
    for z in range(0,ll):
        ligne = ''
        if z < 9:
            ligne = '\x1b[31;1m'+str(z+1)+'  \x1b[36;1m'
        else:
            ligne = '\x1b[31;1m'+str(z+1)+' \x1b[36;1m'
        for r in range(0,lc):
            if r == 8:
                ligne += str(table[z][r]) +'  '
            else:
                ligne += str(table[z][r]) +'  '
        blue(ligne)


def selectPawn(board,ll,lc,player):
    correct = True
    while correct:
        row = raw_input(jaune+'\tSelect a pawn row :'+reg) or 0
        col = raw_input(jaune+'\tSelect a pawn column :'+reg) or 0
        try :
            row,col = int(row)-1,int(col)-1
            correct = False
        except :
            correct = True
    if row < ll and col < lc and row >= 0 and col >= 0:
        if player == 1:selector = 'x'
        elif player == 2:selector = 'o'
        if board[row][col] != selector:
            red('\n\tThis choice is impossible\nTry again')
            row, col = selectPawn(board,ll,lc,player)
    else:
        red('\n\tOut of the board')
        row, col = selectPawn(board,ll,lc,player)
    return row,col

def where(board,nb_ligne,nb_colone,player,row,col):
    correct = True
    while correct:
        col_dest = raw_input(jaune+'\tSelect a destination column :'+reg) or 0
        try :
            col_dest = int(col_dest)-1
            correct = False
        except :
            correct = True

    if col_dest >= 0 and col_dest < nb_colone:
        if col_dest >= col-1:
            if col_dest <= col+1:
                if board[row][col]== 'x':

                    if board[row+1][col_dest]== 'o' and col_dest == col:
                        red('\tcase occupe')
                        where(board,nb_ligne,nb_colone,player,row,col)
                    elif board[row+1][col_dest]== 'x':
                        red('\tVous y etes deja')
                        tour(board,nb_ligne,nb_colone,player)
                    else:
                        board[row+1][col_dest]= 'x'
                        board[row][col]= '.'


                else:
                    if board[row-1][col_dest]== 'x' and col_dest == col:
                        red('\tdestination occuped\nyou can\'t eat this pawn')
                        where(board,nb_ligne,nb_colone,player,row,col)

                    elif board[row-1][col_dest]== 'o':
                        red('\tVous y etes deja')
                        tour(board,nb_ligne,nb_colone,player)
                    else:
                        board[row-1][col_dest]= 'o'
                        board[row][col]= '.'
            else:
                red('\tinvalid column, only 1 case is possible')
                where(board,nb_ligne,nb_colone,player,row,col)
        else:
            red('\tinvalid column, only 1 case is possible')
            where(board,nb_ligne,nb_colone,player,row,col)
    else:
        red('\tout of the board')
        where(board,nb_ligne,nb_colone,player,row,col)

def result(board,ll,lc):
    reste_o = 0
    reste_x = 0
    for x in range(0,ll):
        reste_o += board[x].count('o')
        reste_x +=board[x].count('x')

    if 'x' in board[-1]:
        magenta('Player 1 Win')
        return False
    elif 'o' in board[0]:
        magenta('Player 2 Win')
        return False
    elif reste_x == 0:
        magenta('Player 2 Win')
        return False
    elif reste_o == 0:
        magenta('Player 1 Win')
        return False
    else:
        return True

def tour(tbl,nb_ligne,nb_colone,player):
    yellow('\nPlayer ' + str(player)+' :')
    row, col = selectPawn(tbl,nb_ligne,nb_colone,player)
    where(tbl,nb_ligne,nb_colone,player,row,col)
