t = int(input())
for _ in range(t):
    n = int(input())
    alchol = []
    for _ in range(n):
        S, L = input().split()
        alchol.append([S, int(L)])
    
    alchol = sorted(alchol, key= lambda x:x[1])
    print(alchol[-1][0])
