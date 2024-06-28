# Lists also known as Array.

# Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.

# >>> nums = [ 1, 2, 3, 4, 5, 6 ]
# >>> alph = [ 'a', 'b', 'c', 'd', 'e', 'f' ]
# >>> combine = [ nums, alph]  

# >>> combine                
# [[1, 2, 3, 4, 5, 6], ['a', 'b', 'c', 'd', 'e', 'f']]
# >>> print(combine[1][-1])  
# f

# >>> combine[0][:3] = 99
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only assign an iterable

# >>> combine[0][:3] = 97, 98, 99
# >>> combine                    
# [[97, 98, 99, 4, 5, 6], ['a', 'b', 'c', 'd', 'e', 'f']]

# >>> colors = ['Pink', 'Blue', 'Black', 'Brown']

#       After Slicing - Result is breaked and added
# >>> colors[1:2] = "Lemon"                             // Here string is treated as array. 
# >>> colors               
# ['Pink', 'L', 'e', 'm', 'o', 'n', 'Black', 'Brown']

# >>> colors[1:2]  
# ['Blue']
# >>> colors[1:2] = ["Lemon"]
# >>> colors                 
# ['Pink', 'Lemon', 'Black', 'Brown']

# >>> colors[-1] = "Orange"  
# >>> colors
# ['Pink', 'L', 'e', 'm', 'o', 'n', 'Black', 'Orange']

# >>> colors[6:9:3] = "Red"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: attempt to assign sequence of size 3 to extended slice of size 1

# >>> colors[6:] = "Red"    
# >>> colors            
# ['Pink', 'L', 'e', 'm', 'o', 'n', 'R', 'e', 'd']

# >>> colors[1:1]
# []
# >>> colors[1:1] = ["Green", "Yellow"]                         // Insertion
# >>> colors
# ['Pink', 'Green', 'Yellow', 'Lemon', 'Black', 'Brown']

# >>> colors[3:5]  
# ['Lemon', 'Black']
# >>> colors[3:5] = []                                          // Deletion - Removal - Inserting Nothing
# >>> colors
# ['Pink', 'Green', 'Yellow', 'Brown']

# >>> for color in colors:
# ...     print(color, end=" ")
# ...
# Pink Green Yellow Brown 

# >>> if "Grey" in colors:
# ...     print("YES")
# ... else: 
# ...     print("NO")
# ...
# NO
# >>> colors.append("Grey")
# >>> if "Grey" in colors:  
# ...     print("YES")
# ... else:
# ...     print("NO")
# ...
# YES

# >>> colors.pop()              
# 'Grey'
# >>> colors      
# ['Pink', 'Green', 'Yellow', 'Brown']
# >>> colors.remove("Yellow")
# >>> colors
# ['Pink', 'Green', 'Brown']

# >>> colors.insert(2, "Silver")
# >>> colors.insert(-1, "White")  
# >>> colors                     
# ['Pink', 'Green', 'Silver', 'White', 'Brown']
# >>> colors.insert(-1, "Red")   
# >>> colors
# ['Pink', 'Green', 'Silver', 'White', 'Red', 'Brown']
# >>> colors.insert(2, "Grey")   
# >>> colors
# ['Pink', 'Green', 'Grey', 'Silver', 'White', 'Red', 'Brown']
# >>> colors.insert(-1, "Golden")
# >>> colors
# ['Pink', 'Green', 'Grey', 'Silver', 'White', 'Red', 'Golden', 'Brown']

# >>> colors_copy = colors                      // Same Reference for every " = ".
# >>> colors_copy[2] = "HelloHello"
# >>> colors                       
# ['Pink', 'Green', 'HelloHello', 'Silver', 'White', 'Red', 'Golden', 'Brown']
# >>> colors_copy                  
# ['Pink', 'Green', 'HelloHello', 'Silver', 'White', 'Red', 'Golden', 'Brown']

# >>> colors_copy_second = colors.copy()                    // Different Reference

# >>> squared_nums = [x**2 for x in range(0,10)]
# >>> squared_nums                              
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# >>> range(25) 
# range(0, 25)
# >>> print(range(25))
# range(0, 25)
# >>> print(range(0,25))
# range(0, 25)

# >>> cube_nums = [y**3 for y in range(11,20)]
# >>> cube_nums                               
# [1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]