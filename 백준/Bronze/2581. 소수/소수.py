# 소수를 판별하는 함수
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

M = int(input())
N = int(input())

primes = []
for num in range(M, N + 1):
    if is_prime(num):
        primes.append(num)

if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)