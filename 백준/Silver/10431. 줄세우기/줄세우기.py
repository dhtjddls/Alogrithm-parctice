
p = int(input())
for _ in range(p):
  t = list(map(int, input().split()))
  arr = t[1:]
  cnt = 0
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
        cnt += 1
  print(t[0],cnt)
    
