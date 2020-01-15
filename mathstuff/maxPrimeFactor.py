import sys
import factor

# Project Euler #3

val = 600851475143
facts = factor.factorMap(val)
result = max(facts.keys())
print( "result: ", result)

# testing
chkval = factor.unfactorMap(facts)
print("check: ", val == chkval)
