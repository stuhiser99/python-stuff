from factor import factorMap, unfactorMap

# Project Euler #5

def smallestEvenlyDivisible(value):
    allFactors = [ factorMap(i) for i in range(2, (value+1)) ]
    resultMap = dict()
    for factMap in allFactors:
        for base in factMap:
            if base in resultMap and resultMap[base] > factMap[base]:
                pass
            else:
                resultMap[base] = factMap[base]
    result = unfactorMap(resultMap)
    return result

if __name__ == '__main__':
    print("Initial check: " + repr(factorMap(2520)))
    print("Result 10: " + repr(smallestEvenlyDivisible(10)))
    print("Result 20: " + repr(smallestEvenlyDivisible(20)))

