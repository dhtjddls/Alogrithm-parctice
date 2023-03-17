import sys
input = sys.stdin.readline
n, m = map(int, input().split())
card = list(map(int, input().split()))

min_gap = m
result = 0
for i in card:
    for j in card:
        if i != j:
            for k in card:
                if j != k and i != k:
                    if (i + j + k) <= m and m - (i + j + k) < min_gap:
                        min_gap = m - (i + j + k)
                        result = i + j + k

print(result)



# 최소_갭 = [매우큰수]
# 최소_갭 보다 작으면 = 작은 거
# 해당 값 -> 최소값
# m에 가깝게
# 모든 합 갯수 리스트에 저장한다음에, 해당 리스트 순회하면서 최소 갭 찾기.


# 모든 합 for문으로 돌리고 > 삼중 for
# M 기준으로 각 합과 차이를 찾고 > 단일 for > 삼중안에서 돌리기
# 가장 작은 차이인 숫자 출력
