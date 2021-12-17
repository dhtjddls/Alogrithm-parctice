def po(a, b, c):
    if b == 1:
        return a % c
    popo = po(a,b // 2,c)

    if b % 2 == 0:
        return popo * popo % c
    else:
        return popo * popo * a % c

a, b, c = map(int, input().split())
print(po(a,b,c))
