t = int(input())
for _ in range(t):
    data = input()
    sum = 0
    for i in data:
        if i == '(':
            sum += 1
        if i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum == 0:
        print('YES')
    elif sum > 0:
        print('NO')