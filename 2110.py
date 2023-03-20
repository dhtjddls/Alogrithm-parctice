import sys 

input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()
answer = 0

start, end = 1, house[-1]-house[0]
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    current = house[0]
    for i in range(n):
        if house[i] - current >= mid:
            cnt += 1
            current = house[i]
    if cnt >= c:
        answer = max(mid, answer)
        start = mid + 1
    else:
        end = mid -1

print(answer)
     