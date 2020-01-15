from sieve import sieve

# Project Euler #7

primes = sieve(200000)
print("Len: ", len(primes))
if len(primes) < 10001:
    print("Too short...")
else:
    print("Prime 10001: ", primes[10001])
    