# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 21:27:25 2019

@author: zampochung
"""
singer = ["刘德华", "张学友", "郭富城", "棃明"]
city_jw = ("23.75N, 108.23E", "33.23N, 98.24E", "67.89N, 56.98E")
profile = {"身高":"188", "着色":"黑色", "作者":"毛泽东"}

try:
    ss = input("plz enter one word in 身高 着色 作者: ")
    gg = str(ss)
    if ss in profile:
        pp = profile[ss]
        print(pp)
    else:
        print("not found")
except(ValueError):
     print("ValueError")