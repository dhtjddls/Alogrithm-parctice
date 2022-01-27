N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
sor_B = sorted(B)
num_size = dict()
sum = 0

for i in range(len(B)):
    num_size[i] = sor_B[i]

for i in range(N):
    sum += num_size[i] * A[-i-1]

print(sum)