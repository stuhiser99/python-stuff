import sys

def divideCount(dividend, divisor):
    def divideCountRec(divn, divr, count):
        if divn % divr == 0:
            return divideCountRec(divn // divr, divr, count+1)
        else:
            return (count, divn)
    return divideCountRec(dividend, divisor, 0)

def factorMap(value):
    def factorMapRec(dividend, divisor, factors):
        if dividend == 1:
            return factors
        else:
            count, remain = divideCount(dividend, divisor)
            if count > 0:
                factors[divisor] = count
                return factorMapRec(remain, divisor+1, factors)
            else:
                return factorMapRec(dividend, divisor+1, factors)
    return factorMapRec(value, 2, dict())
    
def factorList(value):
    def factorListRec(dividend, divisor, factors):
        if dividend == 1:
            return factors
        else:
            if dividend % divisor == 0:
                factors.append(divisor)
                return factorListRec(dividend // divisor, divisor, factors)
            else:
                return factorListRec(dividend, divisor+1, factors)
    return factorListRec(value, 2, list())
    
if __name__ == '__main__':
    for s in sys.argv[1:]:
        fl = factorList(int(s))
        print(fl)
        fm = factorMap(int(s))
        print(fm)
