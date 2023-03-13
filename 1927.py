import heapq, sys
input = sys.stdin.readline
heap = []
n = int(input())
for i in range(n):
    val = int(input())
    if val == 0:
        try:
            print(heapq.heappop(heap))  
        except:
            print('0')  
    else:
        heapq.heappush(heap, val)
        


