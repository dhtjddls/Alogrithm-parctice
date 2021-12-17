from typing import Collection


from collections import defaultdict
node = int(input())
line = int(input())
graph = defaultdict(list)

for _ in range(line):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)

def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered

print(len(recursive_dfs(1))-1)