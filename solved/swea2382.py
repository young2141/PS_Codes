import sys
from pprint import pprint
import copy

sys.stdin = open('input.txt','r')

dy = [0,-1,1,0,0]
dx = [0,0,0,-1,1]

def change_dir(d):    
    if d == 1: return 2
    elif d == 2: return 1
    elif d== 3 : return 4
    elif d == 4: return 3

tc = int(input())
for tc in range(1, tc+1):
    answer = 0
    n,time,k = map(int, input().split())
    w = []
    for i in range(k):
        y,x,num,d = map(int, input().split())
        w.append([y,x,num,d])
    
    for t in range(time):
        tmp = [[[] for _ in range(n)] for _ in range(n)]
        for element in w:
            i,j,num,d = element
            y = i + dy[d]
            x = j + dx[d]
            if not 1<= y <n-1 or not 1<= x < n-1:
                tmp[y][x].append([num//2,change_dir(d)])
            else:
                tmp[y][x].append([num,d])
        w = []
        for i in range(n):
            for j in range(n):
                if tmp[i][j]:
                    if len(tmp[i][j]) == 1:
                        w.append([i,j,tmp[i][j][0][0],tmp[i][j][0][1]])
                    else:
                        sumed = 0
                        max_num = 0
                        nd = 0
                        for z in range(len(tmp[i][j])):
                            sumed += tmp[i][j][z][0]
                            if max_num < tmp[i][j][z][0]:
                                max_num = tmp[i][j][z][0]
                                nd = tmp[i][j][z][1]
                        w.append([i,j,sumed,nd])
        
    for element in w:
        answer += element[2]
    print('#{} {}'.format(tc,answer))