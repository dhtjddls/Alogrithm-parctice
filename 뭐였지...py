def rev(x):
    x = list(map(int, x))
    x.reverse()
    x= list(map(str, x))
    X = ''
    for i in range(len(x)):
        X += str(x[i])
        
    return int(X)

a, b = input().split()

print(rev(str(rev(a) + rev(b))))
