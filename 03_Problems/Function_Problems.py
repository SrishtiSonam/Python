# # 1. Basic function syntax
# #       - func to cal square of a number. 
# def square(x):                                      # x - parameter as placeholders
#     return (x**2)
#     # print(x**2)
# square_result = square(4)
# print(square_result)
# print(square(7))


# # 2. Functions with multiple parameters
# #       - func that takes two nums as parameter and return their sum
# def sum_of_two(x,y):
#     return x+y
# num_sum = sum_of_two(3,8)
# alpha_sum = sum_of_two('a','b')
# print(num_sum)
# print(alpha_sum)


# # 3. Polymorphism in function
# #       - WAF multiply that multiplies two nums, but can also accept and multiply strings.
# def multiply(x,y):
#     return x*y
# num_multiply = multiply(6,8)
# alpha_multiply_1 = multiply('hello',7)
# alpha_multiply_2 = multiply(7,'hi')
# print(num_multiply)
# print(alpha_multiply_1)
# print(alpha_multiply_2)


# # 4. Function returning multiple values
# #       - Func return area and parameter for a circle given its radius
# import math
# def circle(r):
#     area = r*r*math.pi
#     parameter = 2*r*math.pi
#     return (area, parameter)
# mycircle_radius = 3
# mycircle_area, mycircle_parameter = circle(mycircle_radius)
# mycircle_statement = "For circle with radius {}, area = {} and parameter = {}."
# print(mycircle_statement.format(mycircle_radius, round(mycircle_area,2), round(mycircle_parameter,2)))


# # 5. Default parameter value
# #       - WAF that greets a user, if no name provided it should greet with a default name.
# def morning_greeting(user = "prince"):
#     greeting_statement = "Good Morning, {}!!!"
#     return greeting_statement.format(user)
# user1 = "ram"
# greet_user1 = morning_greeting(user1)
# greet_user = morning_greeting()
# print(greet_user1)
# print(greet_user)


# # 6. Lambda function - Function with no name - Only for one use - Used in frameworks and liabraries
# #       - to compute cube of a number
# num_cube = lambda x: x**3
# print(num_cube(4))


# # 7. Function with *args            -           special parameters
# #       - func that take variable number of arguments and return their sum.
# def sum_all (*args):
#     sum = 0
#     for i in args:
#         sum+=i
#     return sum
# def sum_nums (*vals):
#     print("vals",vals)                          # Tuple
#     print("*vals",*vals)
#     return sum(vals)
# print(sum_all(1,2,3,4,5,6,7,8,9))
# print(sum_nums(2,4,6,8,10))


# # 8. Function with **kwargs
# #       - accpect any number of keyword argumnets and print then in key:value pair.
# def key_value_print(**kwargs):
#     for i in kwargs:
#         print(i, ":", kwargs[i])
# # key_value_print({"a":1, "b":2, "c":3, "d":4}) -   Wrong
# # key_value_print("a":1, "b":2, "c":3, "d":4)   -   Wrong
# # key_value_print("a"=1, "b"=2, "c"=3, "d"=4)   -   Wrong
# key_value_print(a=1, b=2, c=3, d=4)

# def greet(**kwargs):
#     print("Good", kwargs['time'], kwargs['name'], "!!")
#     # print("Good", time, name, "!!")       -   wrong
#     # print("Good", kwargs[time], kwargs[name], "!!")       -   wrong
# greet(time="morning", name="priya")

# def anotherGreet(time, name):
#     print("Good", time, name, "!!")   
# anotherGreet(name="ram", time="evening")                    # named arguments


# # 9. Generator function with yield                          # yield karna generate karna
# #       - GF that yields even number upto specified limit.
# def yield_even(limit):
#     for i in range(2,limit+1,2):
#         yield i

# for num in yield_even(10):
#     print(num)


################################        Yeild       ####################################


# 10. Recursive Function
#       - RF to calculate factorial
def fact(n):
    if(n<0):
        return -1
    elif n==0:
        return 1
    elif n==1:
        return 1
    return n*fact(n-1)
print(fact(10))