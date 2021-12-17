plate = int(input())
def hanoi(plate, start, mid, target):
    if plate == 1:
        print(start, target)
    else:
        hanoi(plate-1, start, target, mid)
        print(start, target)
        hanoi(plate-1, mid, start, target)

sum = 1
for i in range(plate - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(plate, 1, 2, 3)

# 음 첫번째 가운데 마지막 기둥이 있고, 가장 아래 기둥을 제외한 이전 기둥들을 가운데로 옮기는 n-1 번째의 하노이 식을 불러와서 가운데로 옮기고 다음에 제일 큰 접시를 목표 지점에 옳기고 다시 n-1 번째 하노이 식을 불러와서 마지막 기둥에 옮기는 데, 이때 중요 포인트는 시작에서 마지막 기둥으로 옮겼던 첫번째 와 같은 행위 이지만 지점만 바꿔서 가운데 기둥에서 마지막 기둥으로 가는 식으로 해서 2번 반복해준 것에 이제 제일 아래 접시 중간에 옮기는 것 + 1 해주면 총 이동횟수이다.
