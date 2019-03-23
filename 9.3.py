# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 22:29:40 2019

@author: zampochung
"""


#import os
#os.path.join("E:\Python Learning", "text.txt")
#st = open("test.txt", "w")
#st.write("Hi from python")
#st.close()


#with open("test.txt", "w") as f:
#    f.write("hi hi ni mei ")
    

#import csv
#with open("test.csv", "w") as f:
#    w = csv.writer(f, delimiter = ',')
#    w.writerow(["one", "two", "three"])
#    w.writerow(["four", "five", "six"])
#
#import csv
#with open("test.csv", "r") as f:
#    r = csv.reader(f,delimiter=",")
#    for row in r:
#        print(",".join(row))


#exe_1
#import os
#
#os.path.join ("E:\Publicis_Media Jobs folder\iResearch","艾瑞产品列表.csv")
#import csv
#with open("E:\Publicis_Media Jobs folder\iResearch\艾瑞产品列表.csv", "r") as ii:
#    r = csv.reader(ii, delimiter = ",")
#    for row in r:
#        print(row)

#exe_2
import os
import csv

list_1 =["what is your name: ", "wher are you come from:", "when you go: "]
s=[]
n=0
m=0
try:
   while True:
        print("Type q to quit")
        a = input(list_1[n])
        if a != "q":
            s.append(a)
            m=m+1
        n = n+1
        if n >2:
            n =0
            continue
        if a == "q" or m ==9:
            break
except(ValueError):
    print("ValueError")

with open("ss.txt", "w") as f:
    for i, show in enumerate(s):
        f.write(s[i])
        
with open("ss.csv", "w") as sv:
     w = csv.writer(sv, delimiter = ",")       
     for i, sow in enumerate(s):
         w.writerow(s)





















