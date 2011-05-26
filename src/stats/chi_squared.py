#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Chi-Squared

References:
 2. Python for Bioinformatic, http://telliott99.blogspot.com/2009/08/chi-squared.html
"""

import random,math
nameL = ['RF','LF','RM','LM']
LL = [[],[],[],[]]

N = 100
R = 80
F = 60
for i in range(50000):
	bias = list('R'*R + 'L'*(N-R))
	sex =  list('F'*F + 'M'*(N-F))
	random.shuffle(bias)
	random.shuffle(sex)
	L = [b+s for b,s in zip(bias,sex)]
	for i,case in enumerate(nameL):
		LL[i].append(L.count(case))

print '%-3s %-5s %-5s %-5s %s' % ('', 'mean', 'sd', '95%', 'CI')
for i,L in enumerate(LL):
	n = len(L)
	m = float(sum(L)) / n
	sumsq = sum([(e-m)**2 for e in L])
	sd = math.sqrt(sumsq / n)
	print '%-3s %5.2f %5.2f %5.2f %5.2f' % (nameL[i], m, sd, m-1.96*sd, m+1.96*sd)

"""
    mean  sd    95%   CI
RF  48.01  1.97 44.15 51.88
LF  11.99  1.97  8.12 15.85
RM  31.99  1.97 28.12 35.85
LM   8.01  1.97  4.15 11.88
"""
