import sys

n, m = map(int, sys.stdin.readline().split())

arr = [i for i in range(1, n + 1)]
for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    i, j, k = i - 1, j - 1, k - 1
    arr = arr[:i] + arr[k:j + 1] + arr[i:k] + arr[j + 1:]

print(*arr)