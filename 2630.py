n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

blue_cnt = 0
white_cnt = 0


def cut(x, y, n):
    global white_cnt, blue_cnt
    point = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if point != paper[i][j]:
                cut(x, y, n//2)
                cut(x, y + n//2, n//2)
                cut(x + n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                return
    if point == 0:
        white_cnt += 1

    else:
        blue_cnt += 1

cut(0,0,n)
print(white_cnt)
print(blue_cnt)
# 아직도 2차원 리스트는 헷갈린다..ㅠㅠ 매번 주어진 전체 리스트를 4개의 분면으로 나누어 주면서 체크를 하는 방식이다. 때문에 한번 다름이 체크가 된다면 범위를 총 4개의 사분면으로 설정해서 4개의 재귀를 돌리는 방법 처음 다른게 달라지면 4개의 재귀가 호출되고, 그 다음에는 각각의 요소별로 알아서 돌아가게 끔?! 여튼 그리고 처음에 카운트 횟수를 저장하려고 만들어 둔 블루, 화이트 카운트는 함수 설정 부분 안에서는 적용이 되지 않기 때문에 전역변수로 변환해 주는 글로벌을 사용한 점도 기억하자. 