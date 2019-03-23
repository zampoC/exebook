# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 21:08:56 2019

@author: zampochung
"""
exe_10 = "It was bright cold day in April, and the clocks were striking thirteen."
index1 = exe_10.index(",")
print(exe_10[:index1])


exe_9 = "three"
print(exe_9*3)
print(exe_9 + exe_9 + exe_9)


exe_8 =exe_3.replace(" ","")
print(exe_8)

exe_7="Hemingway"
exe_7.index("m")

exe_6 = "A screaming comes across the sky."
print(exe_6.replace("s", "$"))


exe_5 = ["The","fox","jumped","over","the","fence","."]
exe_5s =" ".join(exe_5)
print(exe_5s.replace(" .", "."))

exe_4 = "Where now? When now? Who now?"
exe_4 = exe_4.replace("?", "?#")
exe_4s = exe_4.split("#")
print(exe_4s)

exe_3  = "aldous Huxley was born in 1894."
print(exe_3.capitalize())

"""exe_2"""
try:
    str1 = input("plz input str1: ")
    str2 = input("str2: ")
    print("Yesterday I wrote a {}. I sent it to {}".format(str1,str2))
except(ValueError):
    print(ValueError)

exe_1 = "Camus"
"""print(exe_1)"""
for i in range(len(exe_1)):
    print(exe_1[i])
    