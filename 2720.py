t = int(input())
coin = [25, 10, 5, 1]
for _ in range(t):
    price = int(input())
    cnt = [0, 0, 0, 0]
    for i in range(len(coin)):
        if price // coin[i] >= 1:
            cnt[i] = price // coin[i]
            price %= coin[i]
            
    print(*cnt)
