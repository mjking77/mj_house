# -*- coding: utf-8 -*-
"""
Created on Tue May 16 21:17:31 2017

@author: mj.chuang
"""

import sympy

a,b=1,100

numbers = range(a,b)
prime_numbers=filter(sympy.isprime,numbers)

print "Range {} - {} : ".format(a,b),

for prime_number in prime_numbers:
    print "{}, ".format(prime_number),

print