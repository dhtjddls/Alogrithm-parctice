from collections import deque
import sys
input = sys.stdin.readline
 
n = int(input())
que = deque([])
 
def push(x):
    que.append(x)
 
def pop():
    if not que:
        return -1
    return que.popleft()
 
def size():
    return len(que)
 
def empty():
    if not que:
        return 1
    return 0
 
def front():
    if not que:
        return -1
    return que[0]
 
def back():
    if not que:
        return -1
    return que[-1]
 
for _ in range(n):
    command = input().split()
    if 'push' in command:
        push(command[1])
    elif 'front' in command:
        print(front())
    elif 'back' in command:
        print(back())
    elif 'size' in command:
        print(size())
    elif 'empty' in command:
        print(empty())
    else:
        print(pop())
