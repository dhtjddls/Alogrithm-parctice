n, k = map(int, input().split())
cnt = 0
while True:
    target = (n//k) * k 
    cnt += (n-target)
    n = target
    if n < k :
        break
    cnt += 1
    n //= k

cnt += (n-1)
    
print(cnt)
# 만약에 if: k로 나누어 질때, 나누고 아니면 -1을 빼준다 라는 형식으로 풀지 않은 이유는 나누어지는 것을 먼저정하는 것이 훨씬 연산의 횟수가 적기 때문이다. 나눠지나? 시도하고 다음 빼기 때문에! 
# 그래서 나눠지는 가장 가까운수 => (n//k) * k 를 먼저구하고 한번에 빼주고, 나누는 방식이 연산이 훨씬 적다.