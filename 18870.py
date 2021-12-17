n = int(input())
x = list(map(int, input().split()))
x_1 = list(sorted(set(x)))
num_dict = dict()

for i in range(len(x_1)):
    num_dict[x_1[i]] = i


for i in x:
    print(num_dict[i],end=' ')