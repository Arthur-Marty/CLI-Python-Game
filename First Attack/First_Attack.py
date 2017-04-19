
from fx import *
from color import *

print('\x1b[39;0m')

size = 0

while size < 1:
    size = raw_input('Size of the board : \x1b[39;0m') or 0
    print('')

    try :
        size = int(size)
    except :
        size = 0

print(size)
tbl = newBoard(size)

# print('Player 1 is x and player 2 is o \n\x1b[39;0m')
display(tbl,size)

# tbl[3][2]=1
# tbl[1][2]=1
# tbl[2][1]=1

partie = True
while partie:
    x = input('x : \x1b[39;0m')-1
    y = input('y : \x1b[39;0m')-1
    if tbl[x][y]==0:
        tbl[x][y]=1
        actualisation(tbl,size)
        partie, coup = notFinish(tbl,size)
        print('il reste '+ str(coup) + ' possibilites')
        display(tbl,size)
    else:
        print('pas possible')



#
# partie = True
# i=0
# while partie:
#     t = notFinish(tbl,size)
#     if t == True:
#         selectSquare(board,size)
#     tour(tbl,size,i%2+1)
#     display(tbl,size)
#     partie = result(tbl,size)
#     i+=1
#
# magenta('in '+str(i)+ ' times')
print('end')
