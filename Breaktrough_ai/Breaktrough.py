from fx import *
from color import *

print('\x1b[39;0m')

nb_ligne = 0
nb_colone = 0

while nb_ligne < 4 or nb_colone < 1:
    nb_ligne = raw_input('nb ligne : \x1b[39;0m') or 0
    nb_colone = raw_input('nb colonne : \x1b[39;0m') or 0
    print('')

    try :
        nb_ligne = int(nb_ligne)
        nb_colone = int(nb_colone)
    except :
        nb_ligne,nb_colone = 0,0

# print(nb_ligne,nb_colone)
tbl = newBoard(nb_ligne,nb_colone)


print('Player 1 is x and player 2 is o \n\x1b[39;0m')
display(tbl,nb_ligne,nb_colone)


partie = True
i=0
while partie:
    tour(tbl,nb_ligne,nb_colone,i%2+1)
    display(tbl,nb_ligne,nb_colone)
    partie = result(tbl,nb_ligne,nb_colone)
    i+=1

magenta('in '+str(i)+ ' times')
print('end')
