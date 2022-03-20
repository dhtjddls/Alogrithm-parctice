n = int(input())


for i in range(n):
    n_list = list(map(int, str(i)))
    if n == i + sum(n_list):
        print(i)
        break
    if i == n-1:
        print(0)
