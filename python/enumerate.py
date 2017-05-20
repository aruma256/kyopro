def enum_primes(n):
    from math import sqrt
    primes = []
    def is_prime(x):
        root_x = sqrt(x)
        for prime in primes:
            if root_x < prime:
                break
            if x % prime == 0:
                return False
        return True
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

