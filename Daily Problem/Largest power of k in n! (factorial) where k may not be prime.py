import math

# Function to compute the prime 
# factorization of a number 'num'
def primeFactors(num):
    factors = []

    count = 0
    while num % 2 == 0:
        num //= 2
        count += 1
    if count > 0:
        factors.append([2, count])

    # Check for odd factors starting from 3
    i = 3
    while i * i <= num:
        count = 0
        while num % i == 0:
            num //= i
            count += 1
        if count > 0:
            factors.append([i, count])
        i += 2

    # If 'num' is still greater than 1, 
    # it's a prime number
    if num > 1:
        factors.append([num, 1])

    return factors

# Function to compute how many times prime p 
# appears in n! using Legendre's formula
def legendre(n, p):
    count = 0
    power = p
    while power <= n:
        count += n // power
        power *= p
    return count

# Function to find the largest power 
# of k that divides n!
def maxKPower(n, k):
    factors = primeFactors(k)
    result = float('inf')

    for prime, expInK in factors:
        
        # Count total exponent of 'prime' in n! 
        # using Legendre’s formula
        countInFact = legendre(n, prime)

        # Divide by its exponent in k
        result = min(result, countInFact // expInK)

    return result

if __name__ == "__main__":
    n = 10
    k = 9
    print(maxKPower(n, k))