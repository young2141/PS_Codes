#sw expert academy 5650 dfs
from pprint import pprint

dir = {'UP':0,'RIGHT':1,'DOWN':2,'LEFT':3}
bounce = [[2,2,1,3,2,2,0,0,0,0,0],
          [3,3,3,2,0,3,1,1,1,1,1],
          [0,1,0,0,3,0,2,2,2,2,2],
          [1,0,2,1,1,1,3,3,3,3,3],]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
def find(w,n,ii,jj,holes,d):
    count = 0
    y,x = ii,jj
    while True:
        y,x = y + dy[d], x + dx[d]
        
        if y <0 or y >=n or x<0 or x >= n:
            return count*2 + 1
        elif y == ii and x == jj:
            return count
        elif w[y][x] == 0:
            pass            
        elif 1 <= w[y][x] <= 5:
            d = bounce[d][w[y][x]]
            count += 1
        elif 6 <= w[y][x] <= 10:
            if holes[w[y][x]][0] == [y,x]:
                y,x = holes[w[y][x]][1]
            else : 
                y,x = holes[w[y][x]][0]            
        elif w[y][x] == -1 :
            return count
    
tc = int(input())
for tc in range(1,tc+1):
    n = int(input())
    w = [[int(x) for x in  input().split()] for _ in range(n)]
    answer = 0 
    holes = [[] for _ in range(11)]
    for i in range(n):
        for j in range(n):
            if 6 <= w[i][j] <= 10:
                holes[w[i][j]].append([i,j])
    for i in range(n):
        for j in range(n):
            if w[i][j] == 0:
                for d in dir.values():
                    answer = max(answer,find(w,n,i,j,holes,d))
    print('#{} {}'.format(tc, answer))
'''
1
10
0 1 0 3 0 0 0 0 7 0
0 0 0 0 -1 0 5 0 0 0
0 4 0 0 0 3 0 0 2 2
1 0 0 0 1 0 0 3 0 0
0 0 3 0 0 0 0 0 6 0
3 0 0 0 2 0 0 1 0 0
0 0 0 0 0 1 0 0 4 0
0 5 0 4 1 0 7 0 0 5
0 0 0 0 0 1 0 0 0 0
2 0 6 0 0 4 0 0 0 4
'''
