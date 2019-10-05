import sys
from pprint import pprint
import copy,itertools
from collections import deque
sys.stdin = open('input.txt','r')

answer = sys.maxsize
n = int(input())
w = [[0 for _ in range(n+1)] for _ in range(n+1)]
population = [0] + list(map(int, input().split()))
tot_pop = sum(population)
cities = list(range(1, n+1))
def is_connected(c):
    visit = [0 for _ in range(n+1)]
    q = deque([c[0]])
    visit[c[0]] = 1
    while q:
        v = q[0]
        q.popleft()
        
        for i in range(1, n+1):
            if w[v][i] and not visit[i] and i in c:
                visit[i] = 1
                q.append(i)
    for val in c:
        if not visit[val]: return False
    return True


for i in range(1,n+1):
    info = list(map(int, input().split()))
    for j in range(info[0]):
        w[i][info[j+1]] = 1
        w[info[j+1]][i] = 1
for i in range(1, n):
    com = itertools.combinations(cities,i)
    for c in com:
        sum_c = 0
        for city in c:
            sum_c += population[city]
        
        diff = abs(sum_c*2-tot_pop)
        if diff < answer:
            other = []
            for j in range(1,n+1):
                if j not in c:
                    other.append(j)
            if is_connected(other) and is_connected(list(c)):       
                answer = diff
if answer == sys.maxsize: answer = -1
print(answer)