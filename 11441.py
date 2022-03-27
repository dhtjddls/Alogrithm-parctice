import sys
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(n):
    dp[i] = dp[i-1] + n_list[i]

m = int(input())
for i in range(m):
    i, j = map(int, input().split())

    print(dp[j-1]-dp[i-2])