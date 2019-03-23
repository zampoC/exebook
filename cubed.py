# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 22:29:40 2019

@author: zampochung
"""

def cubed_(x):
    y=0
    try:
        y = int(x)
        return y*y*y
    except(ValueError):
        print("ValueError")
    