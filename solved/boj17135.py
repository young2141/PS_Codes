# boj 17135 combination
import sys
from pprint import pprint
from itertools import combinations
import copy
sys.stdin = open('input.txt','r')


answer = 0
def shoot(w, pos):
    enemy = []
    for i in range(row):
            for j in range(col):
                if w[i][j] == 1:
                    enemy.append([i,j])
    target = set()
    for p in pos:
        dj = []
        for e in enemy:
            if d >= abs(row-e[0]) + abs(p - e[1]):
                dj.append([abs(row-e[0]) + abs(p - e[1]), e[1],e[0]])
        dj.sort()
        if dj: target.add(str(dj[0][1])+':'+str(dj[0][2]))
    for element in target:
        b,a = map(int,element.split(':'))
        w[a][b] = 0
        
    return len(target)
    

row,col,d = map(int, input().split())
w = [[int(x) for x in input().split()] for _ in range(row)]
save = copy.deepcopy(w)
c = combinations(range(col),3)


for c in c:
    killed = 0 
    w = copy.deepcopy(save)
    while 1:
        killed += shoot(w,c)
        tmp = [[0 for _ in range(col)]for _ in range(row)]
        find = False
        for i in range(row):
            for j in range(col):
                if w[i][j] == 1: 
                    find = True
                    
                    w[i][j] = 0
                    if i+1 < row:
                        tmp[i+1][j] = 1
        w = copy.deepcopy(tmp)            
        if not find:
            answer = max(killed, answer)
            break
print(answer)    
    
    