# 제곱근 으로 소수판별 함수
# 개수가아니라 모두 출력이니까 누적합 X true, false로 판별한 리스트
# 돌면서 true면 출력

def sosu(num):
    if num == 1: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


m, n = map(int,input().split())
for i in range(m, n + 1):
    if sosu(i) == True:
        print(i) 