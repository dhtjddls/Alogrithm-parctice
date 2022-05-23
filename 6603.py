from itertools import combinations

while True:
    s = list(map(int, input().split()))
    if s == [0]:
        break
    else:
        k = s[0]
        del s[0]
        for i in sorted(list(combinations(s, 6))):
            print(*i)
        print()
        
