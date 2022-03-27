n = int(input())
seat = input()
seat = seat.replace('LL', 'b')
cnt = n + 1
for i in seat:
    if i == 'b':
        cnt -= 1

if cnt > n:
    print(n)
else:
    print(cnt)
