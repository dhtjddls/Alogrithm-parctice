n = int(input())
mnt = list(map(int, input().split()))

cnt = 0
start = 0
max_num = 0
for i in mnt:
    if i > start:
        start = i
        cnt = 0
    else:
        cnt += 1
    max_num = max(cnt, max_num)



print(max_num)