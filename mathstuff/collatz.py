import sys

# project Euler #14

def next(value):
    if value % 2 == 0:
        return value // 2
    else:
        return 3*value + 1
        
def sequence(value):
    n = value
    result = list()
    result.append(n)
    while n > 1:
        n = next(n)
        result.append(n)
    return result
    
def longestSeq(limit):
    nums = set(range(1, limit))
    seqs = dict()
    lens = dict()
    ct = 0
    for n in range(limit-1, 0, -1):
    # while len(nums) > 0:
        if len(nums) == 0:
            print("nums exhausted: ct = ", ct, " n = ", n, file=sys.stderr)
            break
        # n = max(nums)
        ct += 1
        if (ct % 1000 == 0):
            print("n: ", n, " nums: ", len(nums), " seqs: ", len(lens), file=sys.stderr)
        if n in nums:
            sq = sequence(n)
            seqs[n] = sq
            lens[n] = len(sq)
            for v in sq:
                if v in nums:
                    nums.remove(v)
    maxlen = max(lens.values())
    mxs = [k for k in lens.keys() if lens[k] == maxlen]
    print("found: ", mxs[0])
    print("len: ", lens[mxs[0]])
    print("seq: ", seqs[mxs[0]])
            
if __name__ == '__main__':
    longestSeq(int(sys.argv[1]))
