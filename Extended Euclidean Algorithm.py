#given two positive integers a and b (here labeled r0 and r1), finds integers x and y such that ax + by = gcd(a, b).
#returns a list [x, y, gcd]. If both a and b are 0, simply returns [0, 0, 0]. This is since, using the formal definition of divisibility,
#where a divides b iff there is some integer k such that b = k * a, all integers divide 0, since 0 = 0 * x for all x. Therefore the gcd
#of zero and a nonzero integer x is abs(x), and the gcd of 0 and 0 is undefined, since all numbers "divide 0" in the formal sense, so any
#integer is a common divisor of 0 and 0, so 0 and 0 have no greatest common divisor. Returning [0, 0, 0] is something of an awkward
#solution for this special case, but I couldn't think of anything better. 
def extendedEE(r0, r1):
    if (r1 == 0):
        if (r0 == 0):
            return [0, 0, 0]
        else:
            sign = r0 // abs(r0)
            return [sign, 0, sign * r0]
    #initial values for "2 steps previously" x and y, "1 step previously" x and y.
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    #compute first remainder and quotient.
    r2 = r0 % r1
    quotient = r0 // r1
    while (r2 != 0):
        #update the x and y variables so that, whatever the current r2 is, it can be written as a linear combination of a and b.
        x0, x1 = x1, x0 - (quotient * x1)
        y0, y1 = y1, y0 - (quotient * y1)
        #assign the "1 step previously" and "current" remainders to "2 steps previously" and "1 step previously"; compute new
        #quotient and remainder.
        r0 = r1
        r1 = r2
        r2 = r0 % r1
        quotient = r0 // r1
    #the gcd of two integers is never negative, but this function will calculate a negative gcd when either both the inputs are negative
    #or the first is positive and the last is negative. The step below ensures that the gcd returned is positive and adjusts the sign of
    #x and y accordingly.
    sign = r1 // abs(r1)
    return [sign * x1, sign * y1, sign * r1]

num1, num2 = 110, 25
test = extendedEE(num1, num2)
print(test)
print(test[0] * num1 + test[1] * num2)