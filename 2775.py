apt = [[0 for _ in range(15)] for _ in range(15)]
for i in range(1,15):
    apt[0][i] = i
    apt[i][1] = 1

for i in range(1, 15):
    for j in range(2, 15):
        apt[i][j] = apt[i][j-1] + apt[i-1][j]

t = int(input())
for t in range(t):
    k = int(input())
    n = int(input())
    print(apt[k][n])

#   점차적으로 쌓아가서 값들을 구하는 문제들은 초기값을 정해주고 나머지는 규칙에 따라 컴퓨터가 계산하게 시키자
#   2차 배열 만드는 방법 꼭 숙지하자!!