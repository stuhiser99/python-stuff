import sys

# Project Euler, #2

def listFibs(limit):
    fibs = [1, 2]
    nxt = 2
    while nxt < limit:
        nxt = fibs[-1] + fibs[-2]
        if nxt < limit:
            fibs.append(nxt)
    return fibs
    
def sumEvenFibs(limit):
    fibs = listFibs(limit)
    sumfibs = sum( filter( lambda x: x%2 == 0, fibs ) )
    return sumfibs
    
if __name__ == '__main__':
    limit = int(sys.argv[1])
    result = sumEvenFibs(limit)
    print(result)
