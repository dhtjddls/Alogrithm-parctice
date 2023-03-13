
# T = int(input())
# for _ in range(T):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#     R = [r1, r2, d]

#     m = max(R)
#     R.remove(m)

#     if d == 0 and r1 == r2:
#         print(-1)
#     elif d == r1 + r2 or m == sum(R):
#         print(1)
#     elif m > sum(R):
#         print(0)
#     else:
#         print(2)
# 원의 방정식을 몰라서 못 풀던 문제 좌표 위의 서로 다른 두 점 사이의 거리를 구하는 원의 방정식을 이용해서 두 좌표사이의 거리를 구하고 그에 따른 두 원의 외접, 내접, 겹쳐서 만나는 점이 2개 혹은 만나지 않는 네 가지 상태를 판단하는 문제였다. 수학을 모르면 못 풀어야지..그럼..그게 맞지ㅠ

import math

t= int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if distance == 0 and r1 == r2:
        print(-1)
    elif distance == (r1 + r2) or distance == abs(r1-r2):
        print(1)
    elif abs(r1-r2) < distance < (r1 + r2):
        print(2)
    else:
        print(0)