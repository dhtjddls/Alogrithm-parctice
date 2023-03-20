n, m = map(int, input().split())
baguni = [0 for _ in range(n+1)]
for _ in range(m):
    i, j, k = map(int, input().split())
    for a in range(i, j+1):
        baguni[a] = k
print(*baguni[1:])