import sys
input = sys.stdin.readline
n = int(input())
member_dict = {}
for _ in range(n):
    name, inout = input().split()
    if inout == 'enter':
        member_dict[name] = 'enter'
    else:
        del member_dict[name]
member_dict = sorted(member_dict.keys(), reverse=True)

for i in member_dict:
    print(i)
