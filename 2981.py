from math import gcd

n = int(input())
m = [int(input()) for _ in range(n)]

m.sort()
result = []
for i in range(1, len(m)):
    result.append(abs(m[i]-m[i-1]))

target = gcd(*result)
print(target)



