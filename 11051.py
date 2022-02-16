from math import factorial
n, k = map(int, input().split())
facto = factorial(n) // (factorial(k) * factorial(n-k))
print(facto % 10007)