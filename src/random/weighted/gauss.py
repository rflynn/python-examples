#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Weighted Random: Gaussian
"""

import random, math

def gauss():
	x = random.random()
	y = random.random()
	z = math.sqrt(-2 * math.log(x)) * math.cos(2 * math.pi * y)
	return z

n = [0]*12

for _ in range(0,100000):
	#r = gauss()
	r = random.gauss(0, 1) # built-in, handy!
	i = int(r+0.5)
	i = (i + (len(n)/2-1)) % len(n)
	n[i] += 1;

# draws bell curve
for x in n:
	print('X' * (int(math.log(x+1)+1)))

