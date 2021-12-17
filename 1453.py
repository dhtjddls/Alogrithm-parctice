pc_list = [0] * 101
N = int(input())
want_list = list(map(int, input().split()))
reject = 0
for i in want_list:
    if pc_list[i] == 0:
        pc_list[i] = 1
    else:
        reject += 1

print(reject)
