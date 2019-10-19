from collections import deque
import sys
sys.stdin = open('input.txt','r')

n = int(input())
for i in range(n):
    s,goal = map(int,input().split())
    visit = set([s])
    q = deque([[s,'']])
    
    while q:
        s,a = q.popleft()
        if s == goal:
            answer = a
            break
        
        D = (s*2)%10000
        if D not in visit:
            visit.add(D)
            q.append([D,a+'D'])
        
        if not s : S = 9999
        else: S = s-1
        if S not in visit:
            visit.add(s)
            q.append([S,a+'S'])
        
        qo, re = s//1000, s%1000
        L = re*10 + qo
        if L not in visit:
            visit.add(L)
            q.append([L,a+'L'])
        
        qo, re = s%10, s//10
        R = qo * 1000 + re
        if R not in visit:
            visit.add(R)
            q.append([R,a+'R'])

    print(answer)