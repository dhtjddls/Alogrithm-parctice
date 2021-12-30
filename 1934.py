t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    one, two = a, b
    while a != 0:
        b = b % a
        a, b = b, a
    print(one * two // b)