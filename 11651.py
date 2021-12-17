N = int(input())
loc = []
for i in range(N):
    x, y = map(int, input().split())
    loc.append([y, x])

sor_loc = sorted(loc)

for y, x in sor_loc:
    print(x, y)

# 문제 잘 안읽어서 x, y 순으로 해버렸다. 사실 그게 아니라 y x 순으로 바꾼다음에 정렬을 해서 출력해주면 되는 문제!
