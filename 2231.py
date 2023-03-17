# n = int(input())

# for i in range(n):
#     n_list = list(map(int, str(i)))
#     if n == i + sum(n_list):
#         print(i)
#         break
#     if i == n-1:
#         print(0)


n = int(input())
# 1~n 까지 for문 돌면서 다해보기 i + i // 자릿수:len(str(i))

for i in range(1, n+1):
    n_list = list(map(int, str(i)))
    s_num = i + sum(n_list)
    if s_num == n:
        print(i)
        break
    if i == n:
        print(0)
 