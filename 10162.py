button = [300, 60, 10]
button_cnt = [0, 0, 0]
t = int(input())
for i in range(len(button)):
    if t // button[i] > 0:
        button_cnt[i] += t // button[i]
        t %= button[i]
if t != 0:
    print(-1)
else:
    print(*button_cnt)