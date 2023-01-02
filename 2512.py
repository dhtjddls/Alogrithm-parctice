def sol():
    n = int(input())
    request = list(map(int, input().split()))
    total_gold = int(input())
    low, high = 0, max(request)
    while low <= high:
        mid = (high + low) // 2
        num = 0
        for i in request:
            if i >= mid: 
                num += mid
            else: 
                num += i
        if num <= total_gold:
            low = mid + 1
        else: 
            high = mid -1
            
    print(high)
    return
sol()