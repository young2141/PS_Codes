import sys
from pprint import pprint
sys.stdin = open('input.txt','r')

def dust_spread(w):
    tmp = [[0 for _ in range(col)]for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if w[i][j]>0 : 
                spreaded = 0
                if i>0 and w[i-1][j] != -1:
                    tmp[i-1][j] += w[i][j]//5
                    spreaded +=1
                if j>0 and w[i][j-1] != -1:
                    tmp[i][j-1] += w[i][j]//5
                    spreaded +=1
                if i < row-1 and w[i+1][j] != -1:
                    tmp[i+1][j] += w[i][j]//5
                    spreaded += 1
                if j < col-1 and w[i][j+1] != -1:
                    tmp[i][j+1] += w[i][j]//5
                    spreaded += 1
                # print(i,j,w[i][j], w[i][j]//5, spreaded)
                w[i][j] = w[i][j] - (w[i][j]//5) * spreaded

    for i in range(row):
        for j in range(col):
            w[i][j] += tmp[i][j]

def clean_air(w,ty,dy):        
    for i in range(ty-1,0,-1): # left
        w[i][0] = w[i-1][0]
    for j in range(0,col-1):   # up
        w[0][j] = w[0][j+1]
    for i in range(0,ty):       # right 
        w[i][col-1] = w[i+1][col-1]
    for j in range(col-1,1,-1): # down
        w[ty][j] = w[ty][j-1]
    w[ty][1] = 0
    for i in range(dy+1,row-1):
        w[i][0] = w[i+1][0]
    for j in range(col-1):
        w[row-1][j] = w[row-1][j+1]
    for i in range(row-1,dy,-1):
        w[i][col-1] = w[i-1][col-1]
    for j in range(col-1,1,-1):
        w[dy][j] = w[dy][j-1]
    w[dy][1] = 0
row,col,time = map(int, input().split())
w = [[int(x) for x in input().split()] for _ in range(row)]
answer = 0
air = []
for i, line in enumerate(w):
    for v in line:
        if v == -1: air.append(i)
    
for t in range(time):
    #pprint(w)
    #print()
    dust_spread(w)
    #pprint(w)
    #print()
    clean_air(w,air[0],air[1])
    #pprint(w)
    #print()

for w_line in w:
    answer += sum(w_line)
print(answer+2)