long = list(map(int, input().split()))
long.sort()
if long[0] + long[1] > long[2]:
    print(sum(long))
else:
    print((long[0] + long[1]) * 2 - 1)