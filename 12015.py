n = int(input())
seq = list(map(int, input().split()))
lst = [0]
for i in seq:
    if lst[-1] < i:
        lst.append(i)
    else:
        start, end = 0, len(lst)
        while start <= end:
            mid = (start + end) // 2
            if lst[mid] < i:
                start = mid + 1
            else:
                end = mid -1
        lst[start] = i
print(len(lst) - 1)