import math

# Project Euler #9

limit = 1000
squares = [ i*i for i in range(limit) ]
triplets = [ (a, b, a*a + b*b) for a in range(2, limit) for b in range(a, limit) ]
print("len triplets: ", len(triplets))

pythags = [ t for t in triplets if t[2] in squares ]
pythag2 = [ ( t[0], t[1], round(math.sqrt(t[2])) ) for t in pythags ]
special = [ t for t in pythag2 if sum(t) == 1000 ]
if len(special) == 1:
    s = special[0]
    print("Triplet: ", s)
    print("Product: ", s[0] * s[1] * s[2])
else:
    print("not found.  ", special)
