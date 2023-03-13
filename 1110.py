# 그냥 구현만 하면 가능할 거 같은?

n = int(input())
cnt = 0
can_change_n = n
while True:
    cnt += 1
    ten = can_change_n // 10
    one = can_change_n % 10
    sum = (ten + one) 
    can_change_n = (sum % 10) + (one * 10)
    if can_change_n == n:
        break
print(cnt)
