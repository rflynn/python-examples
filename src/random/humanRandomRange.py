#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

humanRandomState = {}
def humanRandomRange(key, lo, hi):
    remember = min(int(sqrt(max(hi - lo, 0)) + 1), 10)
    tries = max(remember * 2, 1)
    state = humanRandomState.get(key) or []
    r = None
    for i in xrange(0, tries):
        r = randint(lo, hi)
        if r not in state:
            break
    state.insert(0, r)
    if len(state) > remember:
        state.pop()
    humanRandomState[key] = state
    return r

if __name__ == '__main__':
    from random import randint
    print ''.join(u" ●■◆▲"[randint(1,4)] for _ in xrange(0,50))

    print ''.join(u" ●■◆▲"[humanRandomRange('shapes',1,4)] for _ in xrange(0,50))

