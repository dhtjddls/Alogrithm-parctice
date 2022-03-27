n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

result = 0
cnt = 0

for i in n_list:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(result)