import sys
import copy
from pprint import pprint
sys.stdin = open('input.txt','r')

tc = int(input())
for tc in range(tc):
    n = int(input())
    w = [[int(x) for x in input().split()] for _ in range(2)]
    
    dp = copy.deepcopy(w)
    for i in range(n):
        if i>=2:
            dp[0][i] += max(dp[0][i-2], dp[1][i-1],dp[1][i-2])
            dp[1][i] += max(dp[0][i-1], dp[1][i-2],dp[0][i-2])
        elif i==1:
            dp[0][i] += dp[1][i-1]
            dp[1][i] += dp[0][i-1]
    
    #pprint(dp,width=40)
    print(max(dp[0][n-1],dp[1][n-1]))