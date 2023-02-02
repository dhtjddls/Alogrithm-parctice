from math import gcd
n, m = map(int, input().split(':'))
print(f'{n // gcd(n, m)}:{m // gcd(n, m)}')
