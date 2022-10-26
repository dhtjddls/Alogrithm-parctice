def cal_dist(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2) ** 0.5

w, h, x, y, p = map(int, input().split())
player_num = 0
for _ in range(p):
    player_x, player_y = map(int, input().split())
    if x <= player_x <= x+w and y <= player_y <= y+h:
        player_num += 1
        continue

    r = h/2
    if cal_dist(x, y+r, player_x, player_y) <= r or cal_dist(x+w, y+r, player_x, player_y) <= r:
        player_num += 1

print(player_num)
