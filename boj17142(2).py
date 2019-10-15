import sys
import copy
from pprint import pprint
import itertools
from collections import deque

sys.stdin = open('input.txt', 'r')
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]


def calc(virus, w):
    time = 0
    for i in range(n * n):
        fin = True
        for w_line in w:
            for w_el in w_line:
                if not w_el: fin = False
        if fin: return time
        time += 1
        tmp = []
        for v in virus:
            y, x = v
            for j in range(4):
                ny, nx = y + dy[j], x + dx[j]
                if not 0 <= ny < n or not 0 <= nx < n: continue
                if not w[ny][nx]:
                    w[ny][nx] = 1
                    tmp.append([ny, nx])
        virus = copy.deepcopy(tmp)
    return -1


n, m = map(int, input().split())
w = [[int(x) for x in input().split()] for _ in range(n)]
virus, answer = [], n * n
for i in range(n):
    for j in range(n):
        if w[i][j] == 2: virus.append([i, j])

comb = itertools.combinations(virus, m)
for c in comb:
    answer = min(answer, calc(c, copy.deepcopy(w)))
print(answer)
