from collections import deque
N = int(input())
n = deque()
for i in range(1, N + 1):
    n.append(i)

while len(n) != 1:
    n.popleft()
    n.append(n[0])
    n.popleft()

print(n[0])

# 큐를 구현해서 정해진 행동을 1개가 남을 때까지 반복하면 되는 쉬운 문제였다.