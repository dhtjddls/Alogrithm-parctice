import sys
N = int(sys.stdin.readline())
count = [0] * 10001
for i in range(N):
    num = int(sys.stdin.readline())
    count[num] += 1
for i in range(len(count)):
    for j in range(count[i]):
        print(i)

# 계수 정렬문제였다. 다른 정렬들은 위치를 바꾸는 식인데 이 정렬은 아예 새로운 테이블에 인덱스를 기반으로 숫자를 세서 그대로 출력하는 형식이었다. 테이블에서 인덱스로 바로 호출하니까 시간이 덜 걸리는 형식이었다. 그러나 그럼에도 시간초과가나서 sys를 써야만 했다. 마지막에 2중 반복문에서는 먼저 카운트의 인덱스를 호출하기 위해 한번, 그다음 인덱스의 값을 차례대로 호출하기 위해 두번 사용된 것 같다.
