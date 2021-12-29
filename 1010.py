def fac(n: int)->int:
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    total_bridge = fac(m) // (fac(n) * fac(m - n))
    print(total_bridge)