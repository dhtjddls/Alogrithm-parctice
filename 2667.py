n = int(input())
arr = list(map(int, input().split()))
p, m, g, d = map(int, input().split())
max_v = -1e9
min_v = 1e9


def dfs(cnt, result, p, m, g, d):
    global max_v, min_v
    if cnt == n:
        max_v = max(max_v, result)
        min_v = min(min_v, result)
        return
    if p:
        dfs(cnt + 1, result + arr[cnt], p-1, m, g, d)
    if m:
        dfs(cnt + 1, result - arr[cnt], p, m-1, g, d)
    if g:
        dfs(cnt + 1, result * arr[cnt], p, m, g-1, d)
    if d:
        dfs(cnt + 1, int(result / arr[cnt]), p, m, g, d-1)

dfs(1, arr[0], p, m, g, d)
print(max_v)
print(min_v)

# 백트래킹은 늘 dfs의 뼈대가 된다는 사실을 잊지말자. 재귀적으로 전체 경우의 수를 순회하면서 최대와 최소를 갱신해준다. dfs 상화좌우 순회 문제랑도 비슷하려나?
