import sys
from pprint import pprint
import copy

sys.stdin = open('input.txt','r')

def find_sq(w,y,x,size):
    for i in range(size+1):
        for j in range(size+1):
            if  y+i >= n or x + j >= n or w[y+i][x+j] != 1:
                return False
    return True
    
def clear_sq(w,y,x,size):
    for i in range(size+1):
        for j in range(size+1):
            w[y+i][x+j] = 0
    return w

n = 10
answer = sys.maxsize

q = [[[[int(x) for x in input().split() ]for _ in range(n)],[0,0,0,0,0]]]
while q:
    w = q[0][0]
    used = q[0][1]
    done = True
    q = q[1:]
    leave = False

    for i in range(n):
        for j in range(n):
            if w[i][j] == 1: 
                done = False
                for k in range(4,-1,-1):
                    if find_sq(w,i,j,k):
                        used[k] += 1
                        if max(used) <= 5 and sum(used) <= answer:
                            q.append([clear_sq(copy.deepcopy(w),i,j,k), copy.deepcopy(used)])
                        used[k] -= 1
                leave = True
                break
        if leave : break
                        
    
    if done:
        answer = min(answer, sum(used))
if answer == sys.maxsize : answer = -1
print(answer)
                        