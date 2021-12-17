def fac(n):
    cnt = 1
    if n > 1:
        cnt = n * fac(n-1)
    return cnt

N = int(input())
print(fac(N))    
# 함수안의 함수 재귀를 풀어보았다. 아마 코드잇 재귀 부분을 한번 다시봐야겠다. 그 초기 그니까 기본값이랑 그 이후 규칙값이랑 나눠져있었던 것 같은데 고걸 다시봐야지
