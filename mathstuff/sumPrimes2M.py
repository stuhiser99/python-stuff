from sieve import sieve
from itertools import takewhile

# project Euler #10

primes = sieve(5000000)
if primes[-1] < 2000000:
    raise Exception("too small: " + str(primes[-1]))
    
result = sum( takewhile( lambda x: x < 2000000, primes ) )

print(result)
