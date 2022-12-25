from collections import deque
n, k = map(int, input().split())
nums = deque()
for i in range(1, n+1):
  nums.append(i);
result = list()
while len(nums) != 1:
  for _ in range(k-1):
    nums.append(nums.popleft())
  
  result.append(nums.popleft())

result.append(nums[0])
print(f"<{', '.join(map(str,result))}>")
