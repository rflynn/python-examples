#!/usr/bin/env python
# ex: set ts=4 et:

"""
De-Bruijn Sequence

Generates optimal list containing all permutations of sequences of alphabet K of length N

References:
  1. http://en.wikipedia.org/wiki/De_Bruijn_sequence
  2. http://stackoverflow.com/questions/4008603/how-to-compute-de-bruijn-sequences-for-non-power-of-two-sized-alphabets/4009417#4009417

This is a port of [2].
"""

def de_bruijn(N=4, K=10):
    def de_bruijn1(t, p, N, K, A, Seq):
        if t > N:
            if N % p == 0:
                Seq.extend(A[1:p+1])
        else:
            A[t] = A[t-p]
            de_bruijn1(t+1, p, N, K, A, Seq)
            for j in range(A[t-p]+1, K):
                A[t] = j
                de_bruijn1(t+1, t, N, K, A, Seq)
        return Seq
    return de_bruijn1(1, 1, N, K, [0]*(N+1), [])

assert de_bruijn(0,0) == []
assert de_bruijn(1,1) == [0]
assert de_bruijn(2,2) == [0, 0, 1, 1]
assert de_bruijn(3,3) == [0, 0, 0, 1, 0, 0, 2, 0, 1, 1, 0, 1, 2, 0, 2, 1, 0, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2]
assert de_bruijn(6,2) == [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
assert de_bruijn(2,10) == [0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 2, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 8, 2, 9, 3, 3, 4, 3, 5, 3, 6, 3, 7, 3, 8, 3, 9, 4, 4, 5, 4, 6, 4, 7, 4, 8, 4, 9, 5, 5, 6, 5, 7, 5, 8, 5, 9, 6, 6, 7, 6, 8, 6, 9, 7, 7, 8, 7, 9, 8, 8, 9, 9]

Seq = de_bruijn(2,10)
print Seq
#print ''.join([str(s) for s in Seq])

