import sys
from functools import reduce

# project Euler #20

def factorial(value):
    return reduce(lambda x, y: x*y, range(1, value+1))
    
def sumDigits(value):
    n = value
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s
    
if __name__ == '__main__':
    n = int(sys.argv[1])
    f = factorial(n)
    s = sumDigits(f)
    print("sum: ", s)
