n, m = map(int, input().split())
s = set([input() for i in range(n)])
cnt = 0
for i in range(m):
    t = input()
    if t in s:
        cnt += 1

print(cnt)