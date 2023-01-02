from itertools import combinations
n, s = map(int, input().split())
sequence = list(map(int, input().split()))
cnt = 0

for i in range(1, n+1):
    per = combinations(sequence, i)
    for j in list(per):
        if sum(j) == s:
            cnt += 1

print(cnt);