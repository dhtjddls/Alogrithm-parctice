n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
for i in range(m):
    b.append(list(map(int, input().split())))

c = [[0 for _ in range(k)] for _ in range(n)]

for N in range(n):
    for K in range(k):
        for M in range(m):
            c[N][K] += a[N][M] * b[M][K]

for i in c:
    for j in i:
        print(j, end= ' ')
    print()