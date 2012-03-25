# -*- coding: utf-8 -*-
# ex: set ts=4 et:

"""
Ryan Flynn <parseerror@gmail.com> github.com/rflynn

Challenge: http://beust.com/weblog/2012/02/16/a-new-coding-challenge-2/
1) A function which, passed an int n, returns an array of size n containing
   all the numbers between 0 and n-1 in random order.
   For example, with n=5, valid answers are [0,2,3,1,4], [4,1,2,0,3], etc…
2) Prove that the function you wrote in 1) returns “really random” arrays.

Reasoning:
 The distinct outputs for shuffling [1..n] are n!
 Given a random ordering the probability of any one number appearing in a
 particular position is 1/n.
 Therefore, we can estimate the effectiveness of the entire shuffle by running
 many trials and measuring the frequency of the [0]th element.
"""

import scipy
import random
from array import array

def seqshuffle(n):
    seq = array('L', range(n))
    random.shuffle(seq)
    return seq

if __name__ == '__main__':

    from multiprocessing import Manager, Queue, Pool
    from math import ceil
    import time
    import sys

    def run(args):
        # [0]th value frequency over a set of trials
        n, pop, trials, q = args
        start = time.time()
        v = array('L', [0 for x in range(pop)])
        for _ in xrange(trials):
            try:
                v[seqshuffle(pop)[0]] += 1
            except KeyboardInterrupt:
                pass
        now = time.time()
        q.put((n, pop, trials, v, now - start))

    POP = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    RUNS = range(8, 24+1)

    print 'Usage: python %s <popsize>' % (sys.argv[0],)
    print 'popsize:', POP
    print 'n: %u..%u' % (RUNS[0], RUNS[-1])

    man = Manager()
    q = man.Queue()
    p = Pool()

    # blame http://zachseward.com/sparktweets/
    # http://en.wikipedia.org/wiki/List_of_Unicode_characters#Block_elements
    BLOCKS = u' _▁▂▃▄▅▆▇█'

    popsize = POP

    prevtrials = 0
    prevv = [0 for _ in range(popsize+1)]

    try:
        for n in RUNS:

            # scatter: calculate the amount of work (trials), split it into a bunch of jobs and run
            trials = 2**n
            newtrials = trials - prevtrials
            jobcnt = max(1, newtrials / (2**16))
            jobs = [(n, popsize, newtrials/jobcnt, q) for j in range(jobcnt)]
            last = time.time()
            p.map(run, jobs)

            # gather: wait for all results; sum and display
            v = prevv
            for j in range(len(jobs)):
                _n, _pop, _trials, vj, _elapsed = q.get()
                v = [sum(x) for x in zip(v, vj)]

            prevv = v
            prevtrials = trials

            now = time.time()
            elapsed = now - last

            # print header occasionally
            if n % 25 == RUNS[0]:
                print '%-2s %-3s %-6s %-4s %-5s %-8s %-8s %-5s %-5s %-6s %-6s %s' % (
                    'n', 'pop', 'trials', 'jobs', 'sec', 'mean', 'var', 'std',
                    'min', 'max', 'diff%', 'graph')
            # dump stats
            print '%2u %3u %6s %4u %5.1f %8.1f %8.1f %5.1f %6u %6u %5.1f ' % (
                n, popsize, '2**%u' % (n,), jobcnt, elapsed,
                scipy.mean(v), scipy.var(v), scipy.std(v),
                min(v), max(v), (1.-(min(v)/float(max(v))))*100),
            # silly Unicode histogram
            maxv = max(v)
            for k,freq in enumerate(v):
                scale = float(freq) / maxv
                b = int(ceil(len(BLOCKS) * scale))
                sys.stdout.write(BLOCKS[b-1])
            sys.stdout.write('\n')
    except KeyboardInterrupt:
        try:
            p.terminate()
        except:
            pass

