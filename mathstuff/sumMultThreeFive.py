import sys

# Project Euler #1

def sumMultThreeFive(limit):
    factors = [ f for f in range(limit) if f%3 == 0 or f%5 == 0 ]
    return sum(factors)
    
if __name__ == '__main__':
    limit = int(sys.argv[1])
    result = sumMultThreeFive(limit)
    print(result)
