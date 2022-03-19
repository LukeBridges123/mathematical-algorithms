#A function for randomly generating prime numbers, including very large primes. The function does this by generating random odd numbers
#and testing their primality using the Fermat primality test. Note that the Fermat test is a probabilistic test which incorrectly labels
#some composite numbers ("pseudoprimes") as prime; in particular, the test as implemented here will falsely label "Poulet numbers" (which
#pass the Fermat test with 2 as a base) and "Carmichael numbers" (which pass the Fermat test for all bases) as prime. Therefore this
#function has a chance of generating a composite number; but only a very small chance, as while there are infinitely many pseudoprimes,
#they are quite rare. Note also that the function will never generate 2, even though 2 is a prime, but that doesn't really matter.

import random
#generates a random prime number with n digits. If no argument is passed, defaults to 30 digits.
def randPrime(n:int = 30):
    if (n <= 0):
        print("Error: non-positive integer passed as number of digits. Please only use positive integers.")
        return None
    if (n == 1):
        lowerBound = 1
        upperBound = 10
    else:
        lowerBound = 10**(n-1) + 1
        upperBound = 10**n
    prime = random.randrange(lowerBound, upperBound, 2)
    while (pow(2, prime - 1, prime) != 1): #N.B.: implements "repeated squaring" for fast modular exponentiation
        prime = random.randrange(lowerBound, upperBound, 2)
    return prime