# boj 16637
import sys
from pprint import pprint
import copy
sys.stdin = open("input.txt", "r")

answer = -987654321

def calc(a,b,c):
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c=='*':
        return a*b
    else: print('error')

def dfs(result, index):
    global answer
    if index >= len(op):
        answer = max(answer, result)
        return    
    dfs(calc(result,num[index+1],op[index]), index+1)
    if index+1 < len(op):
        next_result = calc(num[index+1],num[index+2],op[index+1])
        dfs(calc(result, next_result, op[index]),index+2)

n = int(input())
line = input()
num,op = [],[]
for s in line:
    if s.isnumeric(): num.append(int(s))
    else: op.append(s)
dfs(num[0],0)
print(answer)
