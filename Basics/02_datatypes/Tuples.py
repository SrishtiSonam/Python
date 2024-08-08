# Need of tuple ( as lists are there )      -       {   Immutable - References changes but value doesn't   }

# Commonly returned from databases.

# >>> nums = (1,)
# >>> type(nums)
# <class 'tuple'>
# >>> nums = (1)  
# >>> type(nums) 
# <class 'int'>

# >>> nums = (1,2,3,4,5,6,7)
# >>> nums[-5] 
# 3
# >>> nums[1:7:2]
# (2, 4, 6)
# >>> len(nums)
# 7

# >>> nums[3] = 9 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

# >>> more_nums = (11,12,13,14,15)
# >>> all_nums = nums+ more_nums
# >>> all_nums                  
# (1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 15)
# >>> if 11 in all_nums:
# ...     print("YES")
# ... else:
# ...     print("NO")
# ...
# YES

# >>> another_nums = (99,98,97,97,97,96)
# >>> another_nums.count(97)            
# 3

# Unwraping
# >>> tup = (1,2,3)
# >>> (one, two, three) = tup
# >>> one
# 1
# >>> two
# 2
# >>> three
# 3

# >>> t = (1, (2, (3, 4, (5,6,7), 8), 9, 10, 11), 12 ,13 ,14)
# >>> for i in t :
# ...     print(i)
# ...
# 1
# (2, (3, 4, (5, 6, 7), 8), 9, 10, 11)
# 12
# 13
# 14