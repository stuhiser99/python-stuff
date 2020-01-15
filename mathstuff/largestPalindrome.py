import sys

# project Euler #4

def reverseNumber(nbr):
    nextNbr = nbr
    result = 0
    while nextNbr > 0:
        n, r = divmod(nextNbr, 10)
        result = result*10 + r
        nextNbr = n 
    return result
    
def isPalindromeNbr(nbr):
    return nbr == reverseNumber(nbr)
    
def largestPalindrome(bot, top):
    pals = [ x*y for x in range(bot, top) for y in range(x, top) if isPalindromeNbr(x*y) ]
    return max(pals)
    
if __name__ == '__main__':
    pal1 = largestPalindrome(10, 100)
    print("largest 2-digit: ", pal1)
    pal2 = largestPalindrome(100, 1000)
    print("largest 3-digit: ", pal2)
    
