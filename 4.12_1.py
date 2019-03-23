# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 22:20:19 2019

@author: zampochung
"""

def squar(x):
    return x*x

def strr(s='abc'):
    print(s)
    
def abc(x,y=2,z=3):
    return x+y+z


def div2(x):
    an1 = x / 2
    return an1
    
def mul4(x):
    an2 = x * 4
    return an2

def s2f(m):
        x=float(m)
        return x

try:
    m = input('entern a int figure: ')
    n = int(m)
    o=div2(n)
    p=mul4(o)
    print(p)
except(ValueError):
    print('Invalid input.')

try:
    m=input('entry a string: ')
    print(s2f(m))
except(ValueError):
    print('ValueError')    
    
    
    
    
    
    
    
    
    
    
    
