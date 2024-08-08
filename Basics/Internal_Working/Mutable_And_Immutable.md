# Every datatype is called Object here.
# Everything is refered as Object.


# Trying these things in python shell.

# PS C:\Users\Srish\Desktop\Python> python
# Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> myname    
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'myname' is not defined
# >>> username = "Srishti"   //  Getting a space in memory, name as username.    // A container which store value.
# >>> username
# 'Srishti'
# >>> username = "Shreya"   // Here value changed without any error so how strings are immutable.
# >>> username
# 'Shreya' 
# >>> x = 10
# >>> y = x         // "y is pointing at x value." 
# >>> x
# 10
# >>> y
# 10
# >>> x = 5
# >>> x
# 5
# >>> y
# 10


# In our memory, 


# whenever a variable is defined, a portion is allocated for its value.
# like "Srishti" is stored as an object in memory.
# now it is kept as reference.
# Reference is created for the value.
# This can never be changed,

# On changing the value, another menory location/reference is formed.
# First the variable would be pointing to one then to another.
# we never change the value actually we change the refernce pointing.
# Memory reference never changes. (individually)

# Python has automatically garbage collection. 
# If there is nothing referncing a string or data it will automatically deleted. 


# for y = x

# First a reference is created for x with value "10".
# When y is assigned x then, y is also pointing to the same reference.
# On changing the value of x, another reference is created in memory for which x is refered.
#  but reference of y has never changed. 


# For mutable data, values change in memory itself. 
#   {}