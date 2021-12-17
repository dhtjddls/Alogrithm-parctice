import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
pw_dict = dict()

for _ in range(n):
    e, p = sys.stdin.readline().rstrip().split()
    pw_dict[e] = p

for _ in range(m):
    print(pw_dict[sys.stdin.readline().rstrip()])