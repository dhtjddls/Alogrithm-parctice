
def fib(n: int):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n: int):
    fibo_list = [0] * (n+1)
    fibo_list[1], fibo_list[2] = 1, 1
    cnt2 = 0
    for i in range(3, n+1):
        fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
        cnt2 += 1
    return cnt2

n = int(input())

print(fib(n), fibonacci(n))
