import math
T = int(input())
for _ in range(T):
    x, y = map(int,input().split())
    gap = int(y - x)
    if gap <= 3:
        print(gap)
    else:
        n = int(math.sqrt(gap))
        if gap == n ** 2:
            print(2* n - 1)
        elif n ** 2 < gap <= n ** 2 + n:
            print(2 * n)
        else:
            print(2 * n - 1)
# 제곱근의 개념에 익숙하지 않아서 어려웠던 문제이다. 규칙을 발견하기가 쉽지 않아서 대략 여러개의 케이스를 나열해놓고 한참 고민하다 결구 구글링..
# 그치만 구현해내는 로직 그니까 이럴땐 이런 케이스. 저럴땐 저런 케이스 같이 상황을 몇가지 내로 분류하고 정리해서 푸는 게 핵심인듯?