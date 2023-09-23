import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
zeroQueOneStack = list(map(int, input().split()))
targetArr = list(map(int, input().split()))
m = int(input())
appendLeftList = list(map(int, input().split()))

queue = deque([])
for i in range(n):
    if zeroQueOneStack[i] == 0:
        queue.appendleft(targetArr[i])


for i in range(m):
    queue.append(appendLeftList[i])
    print(queue.popleft(), end=" ")
