# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:57:17 2019

@author: zampochung
"""

class Apple():
    
    def __init__(self, c , w, d, t):
        self.color = c
        self.weight = w
        self.day = d
        self.temp = t
        print('creatd')
        
class Circle():
   
    def __init__(self, r):
        self.ran = r

    def area(self):
        import math
        m = math.pi
        return self.ran *2 * m
            
class Triangle():
    
    def __init__(self, l, h):
        self.long = l
        self.high = h        
    
    def area(self):
        return 1/2 * self.long * self.high
    
class Hexagon():
    
    def __init__(self, a):
        self.aline = a
        
    def cacculate_perimeter(self):
        return self.aline*6
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    