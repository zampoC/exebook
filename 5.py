# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 21:27:25 2019

@author: zampochung
"""
rhymes = {"1": "fun",
          "2": "blue",
          "3": "me",
          "4": "floor",
          "5": "live"          
          }

 s = input("enter a number: ")
     if s in rhymes:
        rhyme = rhymes[n]
        print(rhyme)
    else:
        print('not found')