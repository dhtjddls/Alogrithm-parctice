from collections import deque

def printer_deque(n: int, target: int, imp: list):
    imp_idex = deque(list(range(n)))
    cnt = 0
    while imp:
        if imp[0] == max(imp):
            cnt += 1
            imp.popleft()
            if imp_idex.popleft() == target:
                print(cnt) 
        else:
            imp.append(imp.popleft())
            imp_idex.append(imp_idex.popleft())

t = int(input())
for _ in range(t):
    n, target = map(int, input().split())
    imp = deque(list(map(int, input().split())))
    printer_deque(n, target, imp)

