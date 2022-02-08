from fractions import Fraction

n = int(input())
ring = list(map(int, input().split()))
result = []
for i in range(1, n):
    cnt = str(Fraction(ring[0], ring[i]))
    if '/' in cnt:
        print(cnt)
    else:
        print(cnt+'/1')