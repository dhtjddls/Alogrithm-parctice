import sys

input = sys.stdin.readline

tri_num = []
for i in range(1, 46):
    tri_num.append(i * (i + 1) // 2)
answer_list = [0 for _ in range(1001)]

for i in range(len(answer_list)):
    for a in tri_num:
        for b in tri_num:
            for c in tri_num:
                if a + b + c == i:
                    answer_list[i] = 1
t = int(input())
for _ in range(t):
    n = int(input())
    print(answer_list[n])
                    


