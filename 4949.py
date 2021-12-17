
while True:
    string = input()
    if string == ".":
        break
    stk = []
    
    for i in string:
        if i not in '()[]':
            continue
        if i == '(' or i == '[':
            stk.append(i)
        elif (i == ')' and stk and stk[-1] == "(") or (i==']' and stk and stk[-1] == '['):
            stk.pop()
        else:
            stk.append(0)
            break
    if stk:
        print('no')
    else:
        print('yes')

    

