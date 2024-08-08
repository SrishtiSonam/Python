# Numpy + Python === Matlab

# Complex, Boolean(almost numbers 0-1), Decimal, Fraction, sets(internally), 

# Numbers not a single object but a group of objects

# Act and give precision like "Double" of CPP.      // Under the hood every language has same.

# High number ( inifinity ) handling - giving result capability. { e or l are not used in result }
# >>> 99999999999999999999999999999999999999999 * 20
# 1999999999999999999999999999999999999999980
# >>> 99999999999999999999999999999999999999999 * 1.9
# 1.9e+41           { precision }
# >>> 666666666666666666666666666666666666666666 ** 10
#17341529915832613592101475046148114277972357872275567748818777625361987501905197379228776101204084743179393385154702027130008588121729411166996900878931057257531880306441091297058375247675659198292943148910222729461972260326169791190367322054564852922404105065284763501498755271046080373926736729157140679774424630391708581008992531627056851089772900472488949855204999237921048447221798845027011465054446307304103371776


# Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.

# >>> 40+6.78           // Highest precision is prefered
# 46.78
#   // For operations datatype of both the components should be same.   { Mismatched datatype - explicitily }
#   float(), int() - should be used

# >>> 'Hello '+'Shreya'
# 'Hello Shreya'
#   // Operator Overloading as in every other languages.

# >>> x = 3
# >>> y = 6
# >>> z = 8
# >>> x,y,z                 // When dealing with more than one values  
# (3, 6, 8)                 // tuple
# >>> x+1, y*2, z**3        // Performing operations
# (4, 12, 512)

# >>> result = 1/3.0                // Need formating
# >>> result
# 0.3333333333333333

# >>> repr('chai')              //  ????????????????????????????????????????  
# "'chai'"
# >>> str('chai')
# 'chai'
# >>> print('chai')
# chai

# >>> 5 == 5.0                  //  Boolean Values 
# True
# >>> (10**2) > (2**10)
# False
#               {{  Some Short Hand Notation    }}
# >>> -9 < -6 < -3              // -9 < -6 and -6 < -3   
# True
# >>> 8 < 16 < 24               // 8 < 16 and 16 < 24
# True
# >>> 4 == 4 < 3                // 4 == 4 and 4 < 3
# False

# Third party liabrary - Math 
# >>> import math
# >>> math.floor(-7.001)
# -8
# >>> math.trunc(-7.99)         // Take close towards 0 on number line. 
# -7

# >>> h = 3j + 8
# >>> g = 4 + 9j
# >>> h*g 
# (5+84j)

#       {{      Octal, Binary, Decimal, Hexal Values    }}
# >>> 0o20              -           //  0o - starting of octal
# 16
# >>> 0x20              -           //  0x - starting of hexal   
# 32
# >>> 0xFF 
# 255
# >>> 0b1000            -           //  0b - starting of binary 
# 8
#           {{      Methods for them        }}
# >>> oct(100)
# '0o144'
# >>> bin(100)
# '0b1100100'
# >>> hex(100) 
# '0x64'
#           {{      Converting them using int method        }}
# >>> int(33.88)
# 33
# >>> int('33.88') 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '33.88'
# >>> int('1000', 2)
# 8                         // Return decimal values
# >>> int('33', 8)    
# 27
# >>> int('33', 16) 
# 51


#           {{      Bitwise operation       }}
# >>> x = 100
# >>> x << 2                      // Left Shift
# 400
# >>> x >> 2                      // Right Shift
# 25


#            {{      Random       }}
# >>> import random

# >>> random.random()
# 0.3890531476833119
# >>> random.randint(1,100)
# 40
# >>> random.randint(1000,100)
#     raise ValueError(f"empty range in randrange({start}, {stop})")

# >>> l1 = ['a','s','d','f','g']
# >>> random.choice(l1)
# 'g'
# >>> random.choice(1,3,4,5,7,8)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: Random.choice() takes 2 positional arguments but 7 were given
# >>> random.choice([1,3,4,5,7,8]) 
# 8

# >>> l1
# ['d', 's', 'f', 'g', 'a']
# >>> random.shuffle(l1)
# >>> l1
# ['g', 'a', 's', 'd', 'f']


#                   {{      Precision in Python     -   Decimal    }}
# >>> 0.1 + 0.3 + 0.9  
# 1.3
# >>> 0.1 + 0.1 + 0.4  
# 0.6000000000000001
# >>> 0.1 + 0.1 + 0.1 - 0.3
# 5.551115123125783e-17
# >>> (0.1 + 0.1 + 0.1) - 0.3  
# 5.551115123125783e-17

# *********************************
# >>> from decimal import Decimal               -       decimal context manager
# >>> from fractions import Fraction