# Present in different varieties like in other languages.
#   ''  ""      {   """ """     ''' '''     -   Formating is saved here     }


# hello = """ Hello !!
#             My name is Srishti.
#             Nice to meet you.  """
# print(hello)
#  Hello !!
            # My name is Srishti.
            # Nice to meet you.  
# for ch in hello: 
#     if (ch!=" "):
#         print(ch)
# print(len(hello))             // 73


# >>> hello = 'Hello World'
# >>> first_char = hello[0]
# >>> print(first_char)
# H
# >>> print(hello)
# Hello World
# >>> only_hello = hello[:5]
# >>> print(only_hello)
# Hello

# Best example for slicing       =>   num_list = "0123456789"
# >>> num_list = "0123456789"     
# >>> odd_list = num_list[1:11:2]
# >>> print(odd_list)
# 13579


# Mostly used strings are uni-code strings ( letters, alphabets, special characters )


# >>> chai = 'Masala Chai'
# >>> print(chai.lower())
# masala chai
# >>> print(chai.upper()) 
# MASALA CHAI
# >>> next_chai = "    Ginger Tea     "
# >>> print(next_chai.strip())                          // By default spaces " "
# Ginger Tea
# >>> another_chai = next_chai.strip().replace("Ginger", "Lemon")
# >>> print(another_chai)
# Lemon Tea
# >>> print(another_chai.find('on'))
# 3
# >>> print(another_chai.find('On')) 
# -1                // Found nothing
# >>> chais = "Lemon, Ginger, Masala, Mint"
# >>> print(chais.split())                      // By default space
# ['Lemon,', 'Ginger,', 'Masala,', 'Mint']
# >>> print(chais.split(', '))                  // here separator is - ', '     { comma and space }
# ['Lemon', 'Ginger', 'Masala', 'Mint']
# >>> menu = "Masala Chai Ginger Chai Lemon Chai"  
# >>> print(menu.count('Chai'))
# 3


#       ***********************         {} - Placeholders           ******************************
# >>> chai_type = "Green Tea"
# >>> quantity = 3              
# >>> order = "I ordered {} cups of {}."                  
# >>> print(order.format(quantity, chai_type))
# I ordered 3 cups of Green Tea.


#       Joining elements in a list.     
# >>> chai_variety = ['Lemon', 'Ginger', 'Mint', 'Green']
# >>> chai_variety
# ['Lemon', 'Ginger', 'Mint', 'Green']
# >>> print("".join(chai_variety))
# LemonGingerMintGreen
# >>> print(" ".join(chai_variety))
# Lemon Ginger Mint Green
# >>> print(len(" ".join(chai_variety)))
# 23
# >>> for i in " ".join(chai_variety):   
# ...     print(i, end=" ")
# ...
# L e m o n   G i n g e r   M i n t   G r e e n >>>


# >>> said = "He said, \"Ginger Tea is best\". "
# >>> print(said)
# He said, "Ginger Tea is best".
# >>> print("Print \\n Hello")
# Print \n Hello
# >>> slash = r"Print \n Hello"                     // for r"" treated as Raw string
# >>> print(slash)
# Print \n Hello

# >>> address = r"c:\user\pwd\"                         // Ending with \ so treated as \"
#   File "<stdin>", line 1
#     address = r"c:\user\pwd\"
#               ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> address = r"c:\user\pwd\ "                                        // Ending with " "
# >>> address = r"c:\user\pwd\\" 
# >>> print(address)
# c:\user\pwd\\

# without r"" unicode error     -       unicodeescaping
# >>> address = "c:\\user\\pwd\\"  
# >>> address
# 'c:\\user\\pwd\\'
# >>> print(address)
# c:\user\pwd\


# String Containing Question
# >>> str = "hello world"
# >>> print("lo" in str)
# True
