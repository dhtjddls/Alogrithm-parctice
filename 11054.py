n = int(input())
A = list(map(int, input().split()))
decrease_case = A[::-1]
increase = [1 for _ in range(n)]
decrease = [1 for _ in range(n)]
result = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if decrease_case[i] > decrease_case[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

for i in range(n):
    result[i] = increase[i] + decrease[n-i-1] -1

print(max(result))

