import sys
sys.stdin = open('input.txt','r')


n,k = map(int, input().split())
c = []
for _ in range(n):
    x = int(input())
    c.append(x)

dp = [987654321 for _ in range(k+2)]
dp[0] = 0
for i in range(1,k+1):
    for v in c:
        if i-v >= 0:
            dp[i] = min(dp[i],dp[i-v])
    dp[i] += 1
print(dp)
if dp[k] >= 987654321: print(-1)
else: print(dp[k])