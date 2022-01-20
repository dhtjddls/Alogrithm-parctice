n = int(input())

num = list()
for i in range(n):
    num.append(list(map(int, input().split())))

k = 2
for i in range(1, n):
    for j in range(k):
        if j == 0:
            num[i][j] = num[i][j] + num[i-1][j]
        elif i == j:
            num[i][j] = num[i][j] + num[i-1][j-1]
        else:
            num[i][j] = num[i][j] + max(num[i-1][j], num[i-1][j-1])
    k += 1

print(max(num[n-1]))