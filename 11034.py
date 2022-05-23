while True:
    try:
        a, b, c = map(int, input().split())
        left, right = b-a-1, c-b-1
        print(max(left, right))
    except:
        break