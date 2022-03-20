n,m = map(int, input().split())

def numcnt(n, num):
    cnt = 0
    while n != 0:
        n = n // num
        cnt += n
    return cnt

ans = min(numcnt(n, 2)-numcnt(m, 2)-numcnt(n-m, 2), numcnt(n, 5)-numcnt(m, 5)-numcnt(n-m, 5))
print(ans)


