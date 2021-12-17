n, m = map(int, input().split())
instruction = [0]+ [int(input()) for _ in range(n)]
dice = [0]+ [int(input()) for _ in range(m)]
i = 1

for a in range(1, m+1):
    i += dice[a]
    if i >= n:
        print(a)
        break
    i += instruction[i]
    if i >= n:
        print(a)
        break


            

        
