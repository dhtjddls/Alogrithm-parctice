import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
while n >= 0:
    if n % 5 == 0:
        cnt += n // 5
        break
    else:
        n -= 3
        cnt += 1

if n < 0:
    print(-1)
else:
    print(cnt)