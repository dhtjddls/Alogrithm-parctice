def binary(target, list, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if target == list[mid]:
        return 1
    elif target < list[mid]:
        return binary(target, list, start, mid-1)
    else:
        return binary(target, list, mid+1, end)

z = input()
a = sorted(list(map(int, input().split())))

n = input()
t_target = list(map(int, input().split()))

for target in t_target:
    start = 0
    end = len(a)-1
    print(binary(target, a, start, end))

# 이분탐색 기본!
