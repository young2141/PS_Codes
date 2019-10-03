# boj 17070 bfs time eceed
import sys
import copy

n = int(input())
w = [[ int(x) for x in input().split()] for _ in range(n)]

q = [[0,0,0,1]]
answer = 0

while q:
    
    ay,ax,by,bx = q[0]
    q = q[1:]
    if by == n-1 and bx == n-1:
        answer += 1
        continue

    if by - ay == 0 and bx - ax == 1: # 가로
        if bx +1 < n :
            if w[by][bx+1] != 1:                 
                q.append([ay,ax+1,by,bx+1]) #right
        if bx + 1 < n and by + 1 < n:
            if w[by+1][bx+1] != 1 and w[by][bx+1] != 1 and w[by+1][bx] != 1:
                q.append([ay,ax+1,by+1,bx+1]) #diagnol

    if by - ay == 1 and bx - ax == 0: # 세로
        if by +1 < n:
            if w[by+1][bx] != 1:
                q.append([ay+1,ax,by+1,bx])
        if by+1 < n and bx +1 < n:
            if w[by+1][bx+1] != 1 and w[by][bx+1] != 1 and w[by+1][bx] != 1:
                q.append([ay+1,ax,by+1,bx+1])

    if by-ay == 1 and bx-ax == 1: # 대각선
        if by +1 < n:
            if w[by+1][bx] != 1:
                q.append([ay+1,ax+1,by+1,bx])
        if bx +1 < n :
            if w[by][bx+1] != 1:
                q.append([ay+1,ax+1,by,bx+1])
        if by+1 < n and bx +1 < n:
            if w[by+1][bx+1] != 1 and w[by][bx+1] != 1 and w[by+1][bx] != 1:
                q.append([ay+1,ax+1,by+1,bx+1])
    
print(answer)

    