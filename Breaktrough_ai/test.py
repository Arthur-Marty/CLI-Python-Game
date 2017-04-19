

from random import randint


l = 5
c = 5

tbl = [[0] * 5 for i in range(0,l)]

for j in range(0,c):
    tbl[0][j]=1
    tbl[1][j]=1
    tbl[-1][j]=2
    tbl[-2][j]=2
var = 5
for p in range(0,5):
    print(5 + randint(0,2)-1)
