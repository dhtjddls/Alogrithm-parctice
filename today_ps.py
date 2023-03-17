# 1932
n = int(input())
dp = [[0] * i for i in range(1, n+1)]
piramid = []
for i in range(1, n+1):
    piramid.append(list(map(int, input().split())))
dp[0][0] = piramid[0][0]

for i in range(1, n):
    for j in range(len(piramid[i])):
 
        if j == 0:
            dp[i][j] = dp[i-1][j] + piramid[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][-1] + piramid[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1] + piramid[i][j], dp[i-1][j] + piramid[i][j])
            
print(max(dp[n-1]))
