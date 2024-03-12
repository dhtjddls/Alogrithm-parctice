import sys

input = sys.stdin.readline

def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)
n = int(input())
if n == 0:
    print(0)
else:
    remove_cnt = round2(n * 0.15)
    difficulty = sorted([int(input()) for _ in range(n)])
    difficulty = difficulty[remove_cnt: n - remove_cnt]
    print(round2(sum(difficulty) / len(difficulty)))