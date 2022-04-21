#Implementation of the Sieve of Eratosthenes for enumerating all of the primes less than some integer n. Also includes a minor variant of it,
#written for a Project Euler problem, which sums up the primes below n instead of returning a list of them.
def primeSieve(n):
    boolList = [True] * (n + 1);
    primeList = [];
    for i in range (2, (n + 1)):
        if (boolList[i]):
            primeList.append(i)
            j = 2 * i
            while (j < (n + 1)):
                boolList[j] = False
                j += i
    return primeList

def sumSieve(n):
    total = 0;
    boolList = [True] * (n + 1);
    primeList = [];
    for i in range (2, (n + 1)):
        if (boolList[i]):
            total += i
            primeList.append(i)
            j = 2 * i
            while (j < (n + 1)):
                boolList[j] = False
                j += i
    return total
