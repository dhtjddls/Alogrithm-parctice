import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
num_list = [0] * len(num)
cnt = 0
for i in range(n):
    cnt += num[i]
    num_list[i] = cnt

for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        print(num_list[b-1])
    else:
        print(num_list[b-1]-num_list[a-2])