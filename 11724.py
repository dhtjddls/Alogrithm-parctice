from collections import defaultdict
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10000)
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)

visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

cnt = 0
for i in range(1, n+1):
    if visited[i] == False:
        cnt += 1
        dfs(i)

print(cnt)

