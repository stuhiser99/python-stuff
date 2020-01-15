import sys

def divideCount(dividend, divisor, count):
    if dividend % divisor == 0:
        return divideCount(dividend // divisor, divisor, count+1)
    else:
        return count, dividend

def factorMapRec(dividend, divisor, factors):
    if dividend == 1:
        return factors
    else:
        count, remain = divideCount(dividend, divisor, 0)
        if count > 0:
            factors[divisor] = count
            return factorMapRec(remain, divisor+1, factors)
        else:
            return factorMapRec(dividend, divisor+1, factors)

def factorMap(value):
    return factorMapRec(value, 2, dict())

def factorListRec(dividend, divisor, factors):
    if dividend == 1:
        return factors
    elif dividend % divisor == 0:
        factors.append(divisor)
        return factorListRec(dividend // divisor, divisor, factors)
    else:
        return factorListRec(dividend, divisor+1, factors)

def factorList(value):
    return factorListRec(value, 2, list())

if __name__ == '__main__':
    for s in sys.argv[1:]:
        fl = factorList(int(s))
        print(fl)
        fm = factorMap(int(s))
        print(fm)
