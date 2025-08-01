import math

def countNumbers(n):
    c = 0
    limit = int(math.sqrt(n))

    prime = [i for i in range(limit + 1)]

    # Sieve to store smallest prime factor
    for i in range(2, int(math.sqrt(limit)) + 1):
        if prime[i] == i:
            for j in range(i * i, limit + 1, i):
                if prime[j] == j:
                    prime[j] = i

    for i in range(2, limit + 1):
        p = prime[i]
        q = prime[i // prime[i]]

        # Check for p^2 * q^2 form
        if p * q == i and q != 1 and p != q:
            c += 1
        # Check for p^8 form
        elif prime[i] == i and pow(i, 8) <= n:
            c += 1

    return c

n = 100
print(countNumbers(n))