import sys
from pprint import pprint
import copy
from itertools import permutations
sys.stdin = open('input.txt','r')

def do_rotation(sy,sx,ey,ex, w):
    if sy==ey and sx==ex :
        return w        
    
    start = w[sy][sx]
    for i in range(sy,ey):
        w[i][sx] = w[i+1][sx]
    for j in range(sx,ex):
        w[ey][j] = w[ey][j+1]
    for i in range(ey,sy,-1):
        w[i][ex] = w[i-1][ex]
    for j in range(ex,sx,-1):
        w[sy][j] = w[sy][j-1]
    w[sy][sx+1] = start
    return do_rotation(sy+1,sx+1,ey-1,ex-1, w)
    

answer = sys.maxsize
row,col,k = map(int, input().split())
w = [[int(x) for x in input().split()]for _ in range(row)]
rotate = []
for _ in range(k):
    tmp = list(map(int,input().split()))
    rotate.append([tmp[0]-tmp[2]-1,tmp[1]-tmp[2]-1,tmp[0]+tmp[2]-1, tmp[1]+tmp[2]-1])

permutation = permutations(rotate)
for per in permutation:
    tmp = copy.deepcopy(w)
    for i,p in enumerate(per):
        tmp = do_rotation(p[0],p[1],p[2],p[3],copy.deepcopy(tmp))
    for tmp_row in tmp:
        answer = min(answer, sum(tmp_row))       
        
print(answer)