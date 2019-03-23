# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:24:52 2019

@author: zampochung
"""

class Shape():
    def what_am_i(self):
        print("i am a shape")

class Rectangle(Shape):
    def __init__(self, a, b, c):
        self.long = a
        self.mid = b
        self.short = c
            
    def calculate_perimeter(self):
        return self.long + self.mid + self.short

class Square(Shape):
    def __init__(self, a, b):
        self.aline = a
        self.bline = b
        
    def calculate_perimeter(self):
        return self.aline * 2 + self.bline *2
    
    def change_line(self, x):
        self.aline = self.aline + x
        self.bline = self.bline + x
        
class Horse():
    def __init__(self, cor, weit, year, owner):
        self.color = cor
        self.weight = weit
        self.years = year
        self.owner = owner
   
    
class Owner():
    def __init__(self, name):
        self.name = name
        
    
    
    
    
    
    
    
    
    
    
    
    
    
        
