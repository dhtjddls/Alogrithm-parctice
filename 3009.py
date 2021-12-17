x_list = []
y_list = []
for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y = y_list[i]

print(x, y)

#생각보다 조직적인 느낌이 안드는 문제, 일단 x값 리스트와 y 값리스트에서 매칭이되는 애들 빼고 혼자 남은 값이 마지막 퍼즐의 값들이다.


