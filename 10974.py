from itertools import permutations
def all_per(n):
    arr = [i for i in range(1, n+1)]

    return list(permutations(arr, n))



n = int(input())
for i in all_per(n):
    print(*i)