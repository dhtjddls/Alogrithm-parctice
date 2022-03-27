case = 0
while True:
    cnt = 0
    
    L, P, V = map(int, input().split())
    case += 1
    if L == 0 and P == 0 and V == 0:
        break
    else:
        cnt += (V // P) * L
        if V % P > L:
            cnt += L
        else:
            cnt += V % P
        print(f"Case {case}: {cnt}")