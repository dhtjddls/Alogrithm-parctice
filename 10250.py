# 1. 2차원 배열 해당 인덱스에 번호 집어넣기
# 2. 호출
# 
# 1. default case : n % h -> 층 n // h + 1 -> 호
# 2. n % h == 0 case : 

t= int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        print(h * 100 + n // h)
    else:
        print(n % h * 100 + n // h + 1)