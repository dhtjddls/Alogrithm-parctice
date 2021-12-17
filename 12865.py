n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
stuff = []
for _ in range(n):
    stuff.append(list(map(int, input().split())))
# 더 풀어볼게요ㅠㅠㅠ 격자 만들기까지 함..