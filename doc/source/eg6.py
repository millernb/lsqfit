#!/usr/bin/env python
# encoding: utf-8
"""
eg5.py - Code for "y has No Error Bars" and "SVD Cuts and Roundoff Error"

Created by Peter Lepage on 2013-02-12.
Copyright (c) 2013 G. Peter Lepage. All rights reserved.
"""

from __future__ import print_function   # makes this work for python2 and 3
from gvar import *
from lsqfit import nonlinear_fit
import functools
import inspect
import sys

ranseed([123])
ygen = gvar(0.02, 0.2) - 0.005
print (ygen)

y = [gvar(ygen(), ygen.sdev) for i in range(20)]
ystr = [yi.fmt(2) for yi in y]
y = gvar(ystr)
print (ystr[:])

print
log_prior = BufferDict(loga = log(gvar(0.02, 0.02)))  
sqrt_prior = BufferDict(sqrta = sqrt(gvar(0.02, 0.02)))
prior = BufferDict(a = gvar(0.02, 0.02))

stdout = sys.stdout
for p in [prior, log_prior, sqrt_prior]:
	key = list(p.keys())[0]
	sys.stdout = open("eg6-{}.out".format(key), "w")
	def fcn(p, N=len(y)):
		return N*[p['a']]
	f = nonlinear_fit(prior=p, fcn=fcn, data=(y), extend=True)
	print (f)
	print ("a =", f.p['a'].fmt())
sys.stdout = stdout
