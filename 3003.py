pis = list(map(int, input().split()))
correct = [1, 1, 2, 2, 2, 8]
for i in range(len(pis)):
    print(correct[i] - pis[i], end=' ')