import math


def is_prime(t: int):
    if t <= 1:
        return False
    for i in range(2, int(math.sqrt(t)) + 1):
        if t % i == 0:
            return False
    return True


n = int(input())
for _ in range(n):
    t = int(input())
    while True:
        if is_prime(t):
            print(t)
            break
        else:
            t += 1
