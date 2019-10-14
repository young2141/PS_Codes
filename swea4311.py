import sys
import copy
from collections import deque
sys.stdin = open('input.txt','r')

def calc(a,b,op):
    a,b = int(a), int(b)
    if op == 1: 
        if op <= 999 : return a+b 
    elif op == 2: 
        if op >= 0 : return a-b 
    elif op == 3: 
        if op <= 999 : return a*b
    elif op == 4: 
        if b : return a//b    
    return -1

tc = int(input())
for tc in range(1, tc+1):
    n,o,max_hit = map(int, input().split())
    numbers = input().split()
    ops = input().split()
    goal = input()
    answer = sys.maxsize
    tester = list(goal)
    for t in tester:
        if t not in numbers: break
    else: answer = len(goal)
    
    visit = [0 for _ in range(1000)]
    
    q = deque([['', 0]])
    
    while q:
        print(q)
        s,count = q.popleft()
        if count > max_hit : continue
        
        if s == goal:
            answer = min(answer, count)
            continue
            
        candi = [[s,count]]
        if len(s) <3 :
            for num in numbers:
                candi.append([s+num,count+1])
        for cn,cc in candi:
            if cn == '': continue
            cn = int(cn)
            for num in numbers:
                num = int(num)            
                for op in ops:
                    result =  calc(cn,num,op)
                    if result != -1:
                        if visit[result] == 0 or visit[result] > cc +1:
                            visit[result] = cc+1
                            q.append([str(result), cc+1])
                            
    if answer == sys.maxsize: answer = -1
    print(answer)
                
            
        