def slowFib(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return slowFib(n-2) + slowFib(n-1)
def fastFib(n):
    i = 1
    a = 0
    b = 1
    while (i < n):
        temp = b
        b = a + b
        a = temp
        i += 1
    return b
