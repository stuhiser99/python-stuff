import sys
from functools import reduce

def divideCount(dividend, divisor):
    count = 0
    nextDividend = dividend
    while nextDividend % divisor == 0:
        count += 1
        nextDividend = nextDividend // divisor
    return count, nextDividend

def factorMap(value):
    nextDivisor = 2
    nextDividend = value
    factors = dict()
    while nextDividend > 1:
        count, remain = divideCount(nextDividend, nextDivisor)
        if count > 0:
            factors[nextDivisor] = count
            nextDividend = remain
        nextDivisor += 1
    return factors

def factorList(value):
    nextDivisor = 2
    nextDividend = value
    factors = list()
    while nextDividend > 1:
        if nextDividend % nextDivisor == 0:
            factors.append(nextDivisor)
            nextDividend = nextDividend // nextDivisor
        else:
            nextDivisor += 1
    return factors

def unfactorList(factors):
    return reduce( lambda x, y: x*y, factors )

def unfactorMap(factors):
    return reduce( lambda x, y: x*y, [prime ** factors[prime] for prime in factors] )

if __name__ == '__main__':
    for s in sys.argv[1:]:
        fl = factorList(int(s))
        print(fl)
        fm = factorMap(int(s))
        print(fm)
