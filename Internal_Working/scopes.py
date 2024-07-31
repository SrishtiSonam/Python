# # scopes are also called namespaces

# def test():
#     pass

# if True:
#     pass

# # In a scope, inner variables are treated, not related with outer scope. 


# username = "Hi"                 # global variable - standalone

# def func1():
#     # username = "hello"                # Whole file global      
#     print(username)
# func1()

# print(username)


# x = 99
# def func2(x):
#     z = x
#     return z
# print(func2(1))

# def func2(z):                       # Redefining no error     
#     y = z + x
#     return y
# print(func2(5))

# def func3():
#     global x                # Giving global reference - avoid
#     x = 10
# func3()                     # After call the value changes

# print(x)

# def func4():
#     a = 9
#     def func5():
#         print(a)
#     func5()
# func4()        


# def p1():
#     p = 7
#     def p2():
#         print(p)
#     return p2()
# p1()

# def q1():
#     q = 7
#     def q2():
#         print(q)
#     return q2
# funcQ = q1()         # Giving reference of closure - not only the variables + associated variables references               
# funcQ()


# Proper proper closure     -   factory function
def power_func(num):
    def cal_power(x):
        return x**num
    return cal_power
power_call_1 = power_func(2)
power_call_2 = power_func(3)
calculate_power_1 = power_call_1(3)
calculate_power_2 = power_call_2(2)
print(calculate_power_1)
print(calculate_power_2)