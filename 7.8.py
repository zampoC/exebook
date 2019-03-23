# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 21:08:43 2019

@author: zampochung
"""

exe_5_1 = [1,2,3,4,5]
exe_5_2 = [5,4,3,2,1]
exe_5=[]
for i in exe_5_1:
    for j in exe_5_2:
        exe_5.append(i+j)
        print(exe_5)
print(exe_5)



exe_4=[1,2,3,4,6,9,11,25,24,233]

while True:
    m=0
    n = input("please guess a nmuber: ")
    print("type q to quit.")
    if n == "q":
        break
    try:    
      m =int(n)
      if m in exe_4:
          print(m)
    except(ValueError):
        print("ValueError")


exe_3 =[]

for i, show in enumerate(exe_1):
    exe_3.append(i)
    print(exe_3)


exe_2 = 0
for i in range(25, 50):
    exe_2=i
    print(exe_2)

exe_1 = ["The Walking Dead", "Entourage", "the Sopranos", "The Vampire Diaries"]

for show in exe_1:
    print(show)
    