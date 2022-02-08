
n = int(input())
arr = list(map(int, input().split()))
nge = [-1] * n
stack = list()

for i in range(n):
    while stack and (arr[stack[-1]] < arr[i]):
        nge[stack.pop()] = arr[i]
    stack.append(i)

print(*nge)