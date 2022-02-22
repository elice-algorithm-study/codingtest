from itertools import permutations
import math


def is_prime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True


def solution(numbers):
    possible = []
    cnt = 0

    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            j = int(''.join(j))
            if j in possible:
                continue
            else:
                possible.append(j)

    for k in possible:
        if is_prime(k):
            cnt += 1

    return cnt
