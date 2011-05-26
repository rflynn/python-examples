#!/usr/bin/env python

def cycle(s):
	t = (s & 0x1ff) + (s >> 9) + s
	if t < 0:
		t = (t & 0x7fffffff) + 1
	return t

# test
start = n = 0xcafe
n = cycle(n)
cnt = 1
while n != start and cnt <= 0x7fffffff:
	n = cycle(n)
	cnt += 1
print('cnt=%d n=%d' % (cnt, n))

