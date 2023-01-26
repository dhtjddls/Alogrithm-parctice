from itertools import combinations
short = []
for _ in range(9):
    short.append(int(input()))
com = list(combinations(short, 7))
for i in com:
    if sum(i) == 100:
        short = i    
for i in sorted(short):
    print(i)