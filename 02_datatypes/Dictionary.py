# When dealing with no sql data in python.

# In list ordering matters  -    indexing (keys of list)    -   sequencial order

# Key-Value pair comma separated

# >>> counting = dict()
# >>> counting[1] = "one"           // One feild
# >>> counting[2] = "two" 
# >>> counting[3] = "three" 
# >>> counting[4] = "four"  
# >>> counting[5] = "five" 
# >>> counting            
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
# >>> counting.get(3)
# 'three'
# >>> counting[1] = "One"
# >>> counting            
# {1: 'One', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

# >>> for num in counting:
# ...     print(num, " - ", counting[num])
# ...
# 1  -  One
# 2  -  two
# 3  -  three
# 4  -  four
# 5  -  five

# If we iterate over dictionary then we get "Keys" and      { unlike list where we get values over iteration }
#       Dictionary[Keys] = Values

# On iterating over items to access both key value pair,
# >>> for key,value in counting.items():
# ...     print(key, " - ", value)
# ...
# 1  -  One
# 2  -  two
# 3  -  three
# 4  -  four
# 5  -  five

# >>> if 1 in counting:
# ...     print("YES")
# ... else:
# ...     print("NO")
# ...
# YES

# >>> print(len(counting))
# 5

# >>> counting.pop(3)               // pop with key
# 'three'
# >>> counting
# {1: 'One', 2: 'two', 4: 'four', 5: 'five'}

# >>> counting.popitem()            // popitem - last element
# (5, 'five')
# >>> counting
# {1: 'One', 2: 'two', 4: 'four'}

# del - used in many datatype - delete the reference from the memory
# >>> del counting[4]
# >>> counting        
# {1: 'One', 2: 'two'}

# >>> counting_copy_first = counting                    // Same reference 
# >>> counting_copy_first[3] = "Three"
# >>> counting_copy_first             
# {1: 'One', 2: 'two', 3: 'Three'}
# >>> counting                        
# {1: 'One', 2: 'two', 3: 'Three'}
# >>> counting_copy_second = counting.copy()            // Difference reference
# >>> counting_copy_second[4] = 'Four'      
# >>> counting_copy_second            
# {1: 'One', 2: 'two', 3: 'Three', 4: 'Four'}
# >>> counting            
# {1: 'One', 2: 'two', 3: 'Three'}


# >>> info
# {'name': {'firstname': 'Ajay', 'middlename': 'Kumar', 'lastname': 'Singh'}, 'address': {'state': 'Delhi', 'city': {'address city': 'New Delhi', 'original city': 'East Delhi'}, 'locality': 'M.V.Phase - 3'}}
# >>> for key in info:
# ...     print(key, " - ", info[key])  
# ...
# name  -  {'firstname': 'Ajay', 'middlename': 'Kumar', 'lastname': 'Singh'}
# address  -  {'state': 'Delhi', 'city': {'address city': 'New Delhi', 'original city': 'East Delhi'}, 'locality': 'M.V.Phase - 3'}
# >>> info["address"]["city"]["original city"]   
# 'East Delhi'


# >>> squared_nums = {x:x**2 for x in range(10)}                    // list comperihension
# >>> squared_nums                              
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# >>> squared_nums.clear()
# >>> squared_nums
# {}


# >>> keys = [1, 2, 3, 4, 5, 6]
# >>> values = ['a', 's', 'd', 'f', 'g', 'h']
# >>> default_value = 'x'
# >>> dict_with_default = dict.fromkeys(keys, default_value)
# >>> dict_with_default                                     
# {1: 'x', 2: 'x', 3: 'x', 4: 'x', 5: 'x', 6: 'x'}
# >>> dict_with_keys = dict.fromkeys(keys, keys)
# >>> dict_with_keys                            
# {1: [1, 2, 3, 4, 5, 6], 2: [1, 2, 3, 4, 5, 6], 3: [1, 2, 3, 4, 5, 6], 4: [1, 2, 3, 4, 5, 6], 5: [1, 2, 3, 4, 5, 6], 6: [1, 2, 3, 4, 5, 6]} 
# >>>

# Use loops for two arrays.