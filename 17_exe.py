# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:01:40 2019

@author: zampochung
"""

import re

zen = """Although never is 
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain, 
it may be a good
idea. Namesapces
are one honking
great idea -- let's 
do more of thoser!
"""
m = re.findall("^If", zen, re.MULTILINE)



import re
sttr = "two apple is too heavy to catch"

m = re.findall("t[wo]o", sttr, re.IGNORECASE)
print(m)



import re
num = "there 1, 2, 3, 4 5 eggs in the backet"

m = re.findall("\d", num)

print(m)


import re

t = "abc __abc__ __bcdd__ __g2dg3gd__ _dgdlj93839_queen"

found = re.findall("__*.__", t)

for match in found:
    print(match)



import re

text = """Giraffes have aroused
the curiosity of __PLURAL_NOUN__
since earliest times. The
giraffe is the tallest of all
living __PLURAL_NOUN__, but 
scientists are unable to 
explain how it goit its long
__PART_OF_THE_BODY__. The 
giraffe's tremendous height,
which might rech __NUMBER__
__PLURAL_NOUN__, comes from
it legs and __BODYPART__.
"""

def mad_libs(mls):
    """
    :param mls: 字符串
    双下划线部分的内容要由玩家来补充。
    双下划线不能出现在提示语中， 如不能出__hint_init__, 只能是__hint__，
    
    
    
    
    """
    hints = re.findall("__.*?__", mls)
    
    if hints is not None:
        for word in hints:
            q = "Enter a {}".format(word)
            new = input(q)
            mls = mls.replace(word,new,1)
        print("\n")    
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("invaild mls")
mad_libs(text)


"""exe_2"""
import re

strline = "Arizona 479, 501, 870. Carlifornia 209, 213、650."

m = re.findall("\d", strline)
print(m)

"""exe_3"""
import re

str2 = "The ghost that says boo huants the loo goo roo doo."

found = re.findall("[a-z]oo", str2, re.IGNORECASE)

print(found)









