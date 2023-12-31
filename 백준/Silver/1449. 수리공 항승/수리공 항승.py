n, l = map(int, input().split())
spot = list(map(int, input().split()))
spot.sort()

start = spot[0]
count = 1

for i in spot[1:]:
    if i in range(start, start + l):
        continue
    else:
        count += 1
        start = i
print(count)
