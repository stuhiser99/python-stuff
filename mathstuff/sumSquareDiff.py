
# Project Euler #6

def sumSquareDiff(value):
    sumSquares = sum( [ i*i for i in range(1, (value+1)) ] )
    sumVals = sum( [ i for i in range(1, (value+1)) ] )
    squareSum = sumVals ** 2
    diff = squareSum - sumSquares
    return diff
    
if __name__ == '__main__':
    sqd10 = sumSquareDiff(10)
    print("SumSquareDiff 10 = ", sqd10)
    sqd100 = sumSquareDiff(100)
    print("SumSquareDiff 100 = ", sqd100)
    