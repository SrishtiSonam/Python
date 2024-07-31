# Sometimes inner working and given results may vary in python.

# If two variables have same value then they are refered to same data/object value.

# As variable is deleted, it become empty reference for the object which is fixed by garbage collector.
# But python treates strings and numbers differently then other datatypes.

# In python there is a mechanism for counting the pointing references.      { ref_count }
# trying to know this ref_count - not possible through printing
# >>> import sys
# >>> sys.getrefcount
# <built-in function getrefcount>
# >>> sys.getrefcount(89089)
# 3
# >>> sys.getrefcount('srishti')
# 4294967295
# >>> sys.getrefcount('sr')      
# 4294967295


# Datatypes is only for memory not for variable.
# No datatype in python.
# References in memory have datatype.       { Only in memory }


# >>> a = 3                 
#   // It got free 
#       { but python does not collect numbers and string immediatelly due to their high usages}
#       [   Done for optimisation   -   late garbage collection     -    assigning reassigning      ]
# >>> a = 'srishti'
# >>> a = 3.14


# >>> x = 7
# >>> y = 5
# >>> x = x + 5
# >>> x
# 12
# >>> y = y - 8
# >>> y
# -3
# This First calculation is performed and final value is used to make reference object.
#       {   Before calculation all the refered values are collected ( getting values )     }


# >>> mylist = [1,2,3]     
# >>> anotherlist = mylist 
# >>> mylist               
# [1, 2, 3]
# >>> anotherlist
# [1, 2, 3]
# This whole will have a continuous memory allocation - [1,2,3] - refered by both the lists.


# This changed as changed in strings and numbers.
# >>> mylist = "nolist"
# >>> mylist
# 'nolist'


# Now reassigning
# >>> mylist = [1,2,3]              // Second reference created for same value unlike string & number
# >>> mylist
# [1, 2, 3]
# >>> anotherlist       
# [1, 2, 3]


# Changing the value in first list { not affect second list }
# >>> mylist[0] = 44
# >>> mylist         
# [44, 2, 3]
# >>> anotherlist    
# [1, 2, 3]


# Here both the lists have same reference so change in one showed in both
# >>> l1 = ['a','b','c']
# >>> l2 = l1
# >>> l1
# ['a', 'b', 'c']
# >>> l2
# ['a', 'b', 'c']
# >>> l1[0] = 8
# >>> l1        
# [8, 'b', 'c']
# >>> l2
# [8, 'b', 'c']
# >>> l2[2] = [1,2,3]
# >>> l1 
# [8, 'b', [1, 2, 3]]
# >>> l2
# [8, 'b', [1, 2, 3]]


# For same value different references are created.
# >>> p1 = [9, 8, 7]
# >>> p2 = p1
# >>> p2 = [9, 8, 7]
# >>> p1
# [9, 8, 7]
# >>> p2
# [9, 8, 7]
# >>> p1[0] = 'a'
# >>> p1
# ['a', 8, 7]
# >>> p2
# [9, 8, 7]


# Creating other reference through list slicing
# >>> h1 = [4,5,6,7]
# >>> h2 = h1[:]            // Two different references are created for copies.
# >>> h1
# [4, 5, 6, 7]
# >>> h2
# [4, 5, 6, 7]
# >>> h1[1] = 'a'
# >>> h1 
# [4, 'a', 6, 7]
# >>> h2
# [4, 5, 6, 7] 


# >>> import copy
# >>> g1 = [1, [2, [3,4], 5], 6, 7]
# >>> g2 = copy.copy(g1)                // Same reference 
# >>> g3 = copy.deepcopy(g1)            // Another reference
# >>> g1 
# [1, [2, [3, 4], 5], 6, 7]
# >>> g2
# [1, [2, [3, 4], 5], 6, 7]
# >>> g3                    
# [1, [2, [3, 4], 5], 6, 7]
# >>> g1[1][2] = 'a'
# >>> g1 
# [1, [2, [3, 4], 'a'], 6, 7]
# >>> g2
# [1, [2, [3, 4], 'a'], 6, 7]
# >>> g3
# [1, [2, [3, 4], 5], 6, 7]


# >>> m = [12, 34, 56, 78, 90]
# >>> n = m
# >>> o = [12, 34, 56, 78, 90] 
# >>> m == n
# True
# >>> m == o
# True
# >>> n == o
# True
# >>> m is n            // Check Memory Reference
# True
# >>> m is o
# False
# >>> n is o
# False