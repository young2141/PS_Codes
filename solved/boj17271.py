# boj 17271

import sys
import itertools
from collections import deque
sys.stdin = open('input.txt','r')

point = 0
n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
answer = 0
per = [1,2,3,4,5,6,7,8]
per = itertools.permutations(per)
for turn in per:
    turn = list(turn)
    turn.insert(3,0)
    i = 0
    point = 0
    for inning in range(n):
        out_count = 0
        plate = deque()
        while out_count < 3:
            hit = p[inning][turn[i]]
            if hit == 0:
                out_count += 1
            elif hit == 1:
                plate.append(1)
            elif hit == 2:
                plate.append(0)
                plate.append(1)
            elif hit == 3:
                plate.append(0)
                plate.append(0)
                plate.append(1)
            elif hit == 4:
                i = (i+1)%9
                point += plate.count(1)+1
                plate = deque()
                continue
                
            i = (i+1)%9
            if len(plate) >3:
                front = len(plate) - 3
                for _ in range(front):
                    if plate.popleft() == 1:
                        point += 1
                #print(plate)
                
                
    answer = max(point, answer)
print(answer)
