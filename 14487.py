n = int(input())
cost = list(map(int, input().split()))
cost.remove(max(cost))
print(sum(cost))