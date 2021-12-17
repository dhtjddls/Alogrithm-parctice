n = int(input())
cnt = 0
stack = []
result = []
no_message = True
for i in range(n):
    num = int(input())
    while cnt < num:
        cnt += 1
        stack.append(cnt)
        result.append('+')
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        no_message = False

if no_message == False:
    print('NO')
else:
    for i in result:
        print(i) 