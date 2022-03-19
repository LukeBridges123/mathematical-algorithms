#Implementation of the Sieve of Eratosthenes for enumerating all of the primes less than some integer n. Also includes a minor variant of it,
#written for a Project Euler problem, which sums up the primes below n instead of returning a list of them.
def primeSieve(n):
    lim = n + 1;
    boolList = [True] * lim;
    primeList = [];
    currNum = 2;
    while (currNum < lim):
        primeList.append(currNum);
        i = currNum * 2;
        while (i < lim):
            boolList[i] = False;
            i += currNum;
        currNum += 1;
        while (currNum < lim and boolList[currNum] == False):
            currNum += 1;
    return primeList;

def sumSieve(n):
    total = 0;
    lim = n + 1;
    boolList = [True] * lim;
    currNum = 2;
    while (currNum < lim):
        total += currNum;
        i = currNum * 2;
        while (i < lim):
            boolList[i] = False;
            i += currNum;
        i = currNum + 1;
        currNum += 1;
        while (currNum < lim and boolList[currNum] == False):
            currNum += 1;
    print(total);