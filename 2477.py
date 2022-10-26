n = int(input())
w, h = [],[]
res = 0
direction = {i:0 for i in range(1,5)}

for i in range(6):
    d, l = map(int, input().split())
    direction[d] += 1
    if d == 1 or d == 2:
        w.append(l)
    elif d == 3 or d == 4:
        h.append(l)

widx = w.index(max(w))
hidx = h.index(max(h))
if direction[1] == 2 and direction[3] == 2:
    s = max(w) * max(h) - w[widx - 2] * h[hidx - 1]
elif direction[1] == 2 and direction[4] == 2:
    s = max(w) * max(h) - w[widx - 1] * h[hidx - 2]
elif direction[2] == 2 and direction[3] == 2:
    s = max(w) * max(h) - w[widx - 1] * h[hidx - 2]
elif direction[2] == 2 and direction[4] == 2:
    s = max(w) * max(h) - w[widx - 2] * h[hidx - 1]
print(s*n)