import math
num_1, num_2 = map(int, input().split())
GCD_NUM = math.gcd(num_1, num_2)
print(GCD_NUM)
print(num_1 * num_2 // GCD_NUM)