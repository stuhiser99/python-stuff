import math
import sys

# sieve of Eratosthanes

def sieve(limit):
    # allNums = list(range(2, (limit+1)))
    allNums = [ 1 for i in range(limit) ]
    stop = math.ceil(math.sqrt(limit))
    for n in range(2, (stop+1)):
        if allNums[n] != None:
            for j in range(2, math.ceil((limit)/n)):
                factor = n*j
                allNums[factor] = None
    primes = [ i for i in range(2, limit) if allNums[i] != None ]
    return primes
    
if __name__ == '__main__':
    for s in sys.argv[1:]:
        p = sieve(int(s))
        print(len(p), " Primes: ", p)

