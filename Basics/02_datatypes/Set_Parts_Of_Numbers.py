# Sets are also numbers internally

# >>> set1 = {1,2,3,4,5} 
# >>> set2 = {1,3,5,7,9} 

# Apply operations for mathematical sets.

# & - Intersection
# >>> set1 & set2
# {1, 3, 5}

#  | - Union
# >>> set1 | set2  
# {1, 2, 3, 4, 5, 7, 9}

# >>> set1 - set2
# {2, 4}

# >>> set1 - set1 
# set()                 // Empty Curly Parenthesis are Dictionary.      --  Empty set denotion
# >>> type({})
# <class 'dict'>



# >>> type(True)
# <class 'bool'>
# >>> True == 1
# True
# >>> 1 is True
# <stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
# False
# Different in memory but same value
# >>> True + 5
# 6