

n, k = map(int, input().split())
tem_list = list(map(int, input().split()))
point_list = list()
point_list.append(sum(tem_list[:k]))
for i in range(n-k):
    point_list.append(point_list[i] + tem_list[i+k] - tem_list[i])

print(max(point_list))