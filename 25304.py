price = int(input())
knd = int(input())
cost = 0
for i in range(knd):
    a, b = map(int, input().split())
    cost += a * b

if cost == price:
    print('Yes')
else:
    print("No")