import sys
import copy
import itertools
from pprint import pprint
sys.stdin = open('input.txt', 'r')
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]


def calc(virus, w):
    vi = virus[:]
    time = 0
    for _ in range(n * n):        
        time += 1
        tmp = []
        for v in vi:
            y, x = v
            for j in range(4):
                ny, nx = y + dy[j], x + dx[j]
                if not 0 <= ny < n or not 0 <= nx < n: continue
                if not w[ny][nx]:
                    w[ny][nx] = 1
                    tmp.append([ny, nx])
                elif w[ny][nx] == 2:
                    tmp.append([ny, nx])
        vi = copy.deepcopy(tmp)
        if not tmp: break
        print(tmp)
    return sys.maxsize


n, m = map(int, input().split())
w = [[int(x) for x in input().split()] for _ in range(n)]
virus, answer = [], n * n
for i in range(n):
    for j in range(n):
        if w[i][j] == 2: virus.append([i, j])

comb = itertools.combinations(virus, m)
for c in comb:
    answer = min(answer, calc(c, copy.deepcopy(w)))
if answer == n*n: answer = -1
print(answer)
