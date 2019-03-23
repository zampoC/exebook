# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:13:38 2019

@author: zampochung
"""

class Square():
    squs = []
    
    def __init__(self, a):
        self.line = a
        self.squs.append((self.line))
        
    def print_size(self):
        print("""{} by {} by {} by {}""".format(self.line, 
              self.line, self.line, self.line))
        

def check_type(x, y):
    if x is y:
        print(x is y)
    else:
        print("False")
    