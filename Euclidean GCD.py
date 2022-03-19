#Implementation of the Euclidean Algorithm for finding the greatest common divisor of two integers. Compared to the Extended Euclidean
#Algorithm, or at least my implementation of it, is much simpler, as it has less to keep track of, doesn't have to worry as much about
#special cases coming from one or more of the inputs being negative (here, those cases can be taken care of by simply returning the absolute
#value of the gcd), and uses recursion instead of iteration. I thought about including a check for whether b = 0, but that would ruin the
#simplicity a bit. 
def gcd(a:int, b:int):
    r = a % b;
    if (r == 0):
        return abs(b);
    return gcd(b, r);