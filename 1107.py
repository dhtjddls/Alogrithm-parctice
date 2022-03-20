n = int(input())
m = int(input())
m_list = list(map(int, input().split()))

min_cnt = abs(100 - n)

for nums in range(1000001):
    nums = str(nums)

    for i in range(len(nums)):
        if int(nums[i]) in m_list:
            break


        elif i == len(nums) - 1:
            min_cnt = min(min_cnt, abs(int(nums) - n) + len(nums))

print(min_cnt)

