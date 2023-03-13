from collections import deque
n, k = map(int,input().split())
rotate_que = deque(i for i in range(1, n+1))
result = []
while len(rotate_que) > 0:
    rotate_que.rotate(-(k-1))
    result.append(rotate_que.popleft())


result = map(str, result)
answer = ', '.join(result)
print(f"<{answer}>")
