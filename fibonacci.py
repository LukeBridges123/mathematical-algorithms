def slowFib(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return slowFib(n-2) + slowFib(n-1)
def fastFib(n):
    fibList = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        fibList[i] = fibList[i-2] + fibList[i-1]
    return fibList[n]
#print(slowFib(75))
#print(fastFib(75))
