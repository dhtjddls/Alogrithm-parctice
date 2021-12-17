n, m = map(int, input().split())

s = []

def bt(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            bt(i)
            s.pop()

bt(1)