# mathematical algorithms
This repository contains implementations of various mathematical algorithms I've learned about.


The Euclidean Algorithm: simple recursive algorithm that computes the greatest common divisor of two integers. Given two numbers a and b, it computes a % b = r. If r = 0, then b divides a, so gcd(a, b) = b, so the algorithm can return b and terminate. Otherwise, since gcd(a, b) = gcd(b, r), the process can be repeated, computing b % r, and then repeated again, and so on, until a remainder of 0 is found, and then the gcd can be returned. 


Extended Euclidean Algorithm: modification of the Euclidean Algorithm that computes gcd(a, b) as well as integers x and y such that ax + by = gcd(a, b). My implementation is frankly full of kludges needed to avoid divide-by-zero errors and incorrect signs in the output, but I'm not sure if there's a better way to do it. I plan to eventually modify this into a proper solver for linear Diophantine equations.


Sieve of Eratosthenes: classic algorithm for enumerating all of the primes up to some number. Also includes a minor variant which sums up all the primes up to some number.


Fermat primality test: the main attraction of the "Primality Test Comparison" file. Fermat's Little Theorem guarantees that, if p is a prime and a is an integer not divisible by p, then a^(p-1) is congruent to 1 (mod p). This necessarily implies that, if a^(p-1) is not congruent to 1 (mod p), then p is composite. As such, Fermat's Little Theorem can be used as a (very, very fast) primality test: take some number relatively prime to the number being checked (here 2 is used), raise it to p-1 mod p, and if the result is not 1, p must be composite. However, some composites will produce 1 (and thus be counted as prime) for any base, so this is an unreliable test--but only slightly, as such "pseudoprimes" are rare. This file also includes two versions of trial division so that the Fermat test's speed can be better appreciated.


Random prime generator: does exactly what it says on the tin; generates a random prime number of n digits. Since the Fermat test is used, has a very slight chance of generating a composite number.

Fibonacci: naive, exponential-time and improved, polynomial-time algorithms for calculating the nth Fibonacci number. (Assuming that the 1st and 2nd Fibonacci numbers are both 1.)
