import heapq, sys

input = sys.stdin.readline

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, (-num))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)