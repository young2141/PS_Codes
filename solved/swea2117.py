import sys
from pprint import pprint

sys.stdin = open('input.txt','r')

def check(i, j, l):
    if l <0 : return 0
    if not 0<=i<n or not 0<=j<n: return 0
    ret = w[i][j] * m
    for z in range(1,l+1):
        if j+z <n:
            if w[i][j+z] : ret+= m
        if j-z >= 0:
            if w[i][j-z] : ret += m
    return ret

tc = int(input())
for tc in range(1,tc+1):
    n,m = map(int, input().split())
    w = [[int(x) for x in input().split()]for _ in range(n)]
    
    total_house = 0
    for w_line in w:
        for element in w_line:
            if element == 1: total_house +=1
    
    k = 1
    answer = 0
    while total_house*m >= k*k+(k-1)*(k-1):
        for i in range(n):
            for j in range(n):
                if k==3 and i==j:
                    a=1
                fee = 0
                for l in range(1,k):
                    fee += check(i+l,j,k-l-1)
                fee += check(i,j,k-1)       
                for l in range(1,k):
                    fee += check(i-l,j,k-l-1)

                if k*k+(k-1)*(k-1) <= fee:
                    answer = max(answer, fee//m)        
        #print('{}: {}'.format(k, answer))
        k += 1
    print('#{} {}'.format(tc, answer))
                    