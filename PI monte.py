# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:05:33 2019

@author: User
"""
from random import random
from math import pi 


N = 0
X = 0
Y = 0
NT = 0 
while N < 100000000:
    X = random()
    Y = random()
    XY = X*X + Y*Y    
    if XY <= 1:
        NT = NT + 1
    N = N+1    
PI = 4*NT / N
PIT = PI/pi
print(N)
print(PI)
print(PIT)