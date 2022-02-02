n = int(input())
arr = list(map(int, input().split()))
dp = len(arr) * [0]
dp[0] = arr[0]
for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))