# PS C:\Users\Srish\Desktop\Python> python
# Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.


#   ---------------------   Numbers     -----------------------
# >>> 2.5 * 89
# 222.5                     // Python supports high precision.
# >>> 2.55555 * 89
# 227.44395000000003    
# >>> 2.55555 ** 89
# 1.8454829569343113e+36            // Python handles bog numbers easily.
# >>> import math
# >>> math.pi
# 3.141592653589793
# >>> import random
# >>> random.random()
# 0.5488842185348033
# >>> random.choice([1,2,3,4,5])
# 1
# >>> random.choice([1,2,3,4,5])
# 5


#   ----------------------------    Strings     -------------------------------
# >>> username = "Srishti"
# >>> len(username)
# 7
# >>> username[3]               // Internally treated as list for indexing.
# 's'
# >>> username[-3]
# 'h'
# >>> username[:3] 
# 'Sri'
# >>> username[3:]
# 'shti'
# >>> dir(username)             // Things we can do - getting help
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


#       --------------------------      List (array)        -----------------------------
# >>> mylist = [123, 'chai', 3.14, "d", [1, [2,3, [4,5,6]]] ]
# >>> len(mylist)
# 5
# >>> for i in mylist:
# ...     print(i)
# ...
# 123
# chai
# 3.14
# d
# [1, [2, 3, [4, 5, 6]]]
# >>> mylist[-3]
# 3.14


#       -------------------------------     Dictionary      -----------------------------
# >>> myfoodmenu = {'first':'oreo shake', 'next':'kitkat shake', 'coffee':'cold', 'always':'panner paratha' }
# >>> myfoodmenu['coffee'] 
# 'cold'
# >>> myfoodmenu['coffe']                           // KeyError
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'coffe'


#       -------------------------       Tuples          ------------------------------------
# >>> myTup = (1,2,3)     
# >>> mySecondTup = ('a',)
# >>> mySecondTup[0]  
# 'a'
# >>> len(myTup) 
# 3

