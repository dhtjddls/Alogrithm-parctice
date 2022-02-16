h, m = map(int, input().split())
cook = int(input())
if m + cook >= 60:
    h += (m + cook) // 60
    m = (m + cook) % 60
else:
    m += cook
if h >= 24:
    h = h % 24

print(h, m)