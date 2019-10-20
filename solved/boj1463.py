n = int(input())
dp = [987654321 for _ in range(1000010)]
dp[1] = 0

for i in range(1,n+1):
    dp[i+1] = min(dp[i+1],dp[i] + 1)
    if i*2 <= 1000000 : dp[i*2] = min(dp[i*2], dp[i] + 1)
    if i*3 <= 1000000 : dp[i*3] = min(dp[i*3], dp[i] + 1)

print(dp[n])
