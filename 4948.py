# def prime_num(n):
#     if n == 1:
#         return False
#     else:
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True

# save_list = []
# for i in range(2, 246913):
#     if prime_num(i):
#         save_list.append(i)

# n = int(input())

# while True:
#     cnt = 0
#     if n == 0:
#         break
#     for i in save_list:
#         if n < i <= 2 * n:
#             cnt += 1
#     print(cnt)
#     n = int(input())

# 처음에는 2581번 문제를 풀때와 마찬가지로 n값이 입력될 때마다 2부터 입력된 값을 돌면서 나눠지는 값이 2개 이상이면 넘어가는 식으로 소수를 판별했다. 하지만 그럴 경우 매번 값을 돌고, 2개 이상이 나올 때까지 계속 판별을 하기 때문에 계속해서 시관초과가 나왔다. 때문에 먼저 소수판별과정은 소수의 특징을 이용해 제곱근 까지만 소수 판별을 진행하는 방식으로 바꾸었고, 매번 값을 처음부터 도는게 아니라 전체범위 n~2n까지의 수를 모두 돌면서 리스트에 소수값만 한번 저장해두고 입력값의 범위가 비교하는 식으로 해결하였다.



# 1. 소수 판별
# 2. n ~ 2n 사이를 돌면서 소수판별
# 3. 출력?
# 4. 0 입력시 종료

def sosu(num):
    if i == 1: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


memo = [False, False]
for i in range(2, 123456*2 + 1):
    memo.append(sosu(i))


while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    for i in range(n+1, 2 * n + 1):
        if memo[i]:
            cnt += 1
    print(cnt)
    