
from color import *

# i've choice to call my variables ll for n (because it's len ligne ) and lc for p (because it's len collumn )
# it's easier
def newBoard(size):
    tbl = [[0]*size for i in range(size)]
    return tbl

def display(table,size):
    test = '   '
    for v in range(1,size+1):
        if v == 9:
            test += str(v)+' '
        elif v <10:
            test += str(v)+'  '
        else:
            test += str(v)+' '
    red(test)
    for z in range(0,size):
        ligne = ''
        if z < 9:
            ligne = '\x1b[31;1m'+str(z+1)+'  \x1b[36;1m'
        else:
            ligne = '\x1b[31;1m'+str(z+1)+' \x1b[36;1m'
        for r in range(0,size):
            if table[z][r] == 1:
                ligne += 'o' +'  '
            elif table[z][r] == 2:
                ligne += '.' +'  '
            else:
                ligne += '.' +'  '

        blue(ligne)

#fonction qui change les cases ou le joueur ne peux pas poser
def actualisation(board,size):
    for a in range(0,size):                         # double boucle pour passer par toute les cases du tableau
        for b in range(0,size):
            if board[a][b] == 1:                    # condition pour verifier que il y ais bien un pion
                # calculs des position orthogonales indisponibles pour l'adversaire
                for c in range(0,size):
                    board[a][c] = 2                 # a est fixe et c varie de 0 a size pour parcourir toute la ligne du pion
                    board[c][b] = 2                 # b est fixe et c varie de 0 a size pour parcourir toute la colonne du pion

                # calculs des position de la diagonale inferieure droite, indisponibles pour l'adversaire
                for add in range(a+1,size):
                    addb = add -a +b               # addb augmente de la colonne du pion a size
                    if add < size and addb < size:  # Cete condition isole les cas ou add et addb depacent du tableau
                        board[add][addb] = 2        # add augmente pour parcourir toute les lignes inferieures au pion


                # calculs des position de la diagonale supperieure gauche, indisponibles pour l'adversaire
                for add in range(0,a+1):
                    addb = b - add                  # addb diminue de la colonne du pion a 0
                    adda = a - add                  # adda diminue de la ligne du pion a 0
                    if adda >= 0 and addb >= 0:     # Cete condition isole les cas ou add et addb depacent du tableau
                        board[adda][addb] = 2       # changement pour adda et addb


                # calculs des position de la diagonale inferieures gauche, indisponibles pour l'adversaire
                i=0                                 # initialisation de conteur
                for add in range(a,size):
                    addb = b - i                    # addb diminue de la colonne du pion a 0
                    i +=1                           # ajout de 1 au compteur
                    if add < size and addb >=0:     # Cete condition isole les cas ou add et addb depacent du tableau
                        board[add][addb] = 2        # changement pour add et addb

                # calculs des position de la diagonale supperieure droite, indisponibles pour l'adversaire
                j=0                                 # initialisation de conteur
                for add in range(b,size):
                    adda = a - j                    # adda diminue de la ligne du pion a 0
                    j +=1                           # ajout de 1 au compteur
                    if adda >= 0 and add < size:    # Cete condition isole les cas ou add et addb depacent du tableau
                        board[adda][add] = 2        # changement pour adda et add

                board[a][b]=1                       # Remise du pion en 1 car il est change en 2 par le calcul orthogonal

#fonction qui viens determiner si il reste des possibilitees et return True si c'est le cas
def notFinish(board,size):
    pos_possible = 0
    for a in range(0,size):
        for b in range(0,size):
            if board[a][b]==0:
                pos_possible += 1
    if pos_possible > 0:
        return True , pos_possible
    else:
        return False,0


































# ------------------------------------------------------------------------------------------------------------------------------------------------


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
            yellow('\nThis choice is impossible\nTry again')
            row, col = selectPawn(board,ll,lc,player)
    else:
        yellow('\nOut of the board')
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
                        yellow('case occupe')
                        where(board,nb_ligne,nb_colone,player,row,col)
                    elif board[row+1][col_dest]== 'x':
                        print('Vous y etes deja')
                        tour(board,nb_ligne,nb_colone,player)
                    else:
                        board[row+1][col_dest]= 'x'
                        board[row][col]= '.'


                else:
                    if board[row-1][col_dest]== 'x' and col_dest == col:
                        yellow('destination occuped\nyou can\'t eat this pawn')
                        where(board,nb_ligne,nb_colone,player,row,col)

                    elif board[row-1][col_dest]== 'o':
                        print('Vous y etes deja')
                        tour(board,nb_ligne,nb_colone,player)
                    else:
                        board[row-1][col_dest]= 'o'
                        board[row][col]= '.'
            else:
                yellow('invalid column, only 1 case is possible')
                where(board,nb_ligne,nb_colone,player,row,col)
        else:
            yellow('invalid column, only 1 case is possible')
            where(board,nb_ligne,nb_colone,player,row,col)
    else:
        yellow('out of the board')
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
