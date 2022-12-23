n = int(input())
nums = set(list(map(int, input().split())))
nums = list(nums)
nums.sort()

for i in nums:
    print(i, end=' ')