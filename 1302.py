from collections import defaultdict
sold_dic = defaultdict(int)
n = int(input())
max_list = list()

for _ in range(n):
    k = input()
    sold_dic[k] += 1

for k, v in sold_dic.items():
    if max(sold_dic.values()) == v:
        max_list.append(k)

max_list.sort()

print(max_list[0])