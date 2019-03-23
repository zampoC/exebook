# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 22:23:25 2019

@author: zampochung
"""
import random
nums = [random.randint(0,20), random.randint(0,15), random.randint(0,34), random.randint(0,100), ]


import statistics

import cubed
print(cubed.cubed_(statistics.variance(nums)))
print(statistics.variance(nums))
