# Passing a function through a decorator



# # 1. Timing Function Execution
# #       - Write a decorator that measures the time a function takes to execute.

import time 

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"{func.__name__} ran in {end_time-start_time} time.")
#         return result
#     return wrapper

# @timer
# def example_func(n):
#     time.sleep(n)

# example_func(4)



# 2. Debugging Function Calls
#       - Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        args_values = ', '.join(str(arg) for arg in args)               # Taking all the comma separated values and # Give iterable list
        kwargs_values = ', '.join(f'{k} = {v}' for k, v in kwargs.items())
        print(f"Calling: {func.__name__} with args {args_values} and kwargs {kwargs_values}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("Hello!!")

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!!")

hello()
greet("chai", greeting='Hanji')



# 3. Cache Return Values
#       - Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing of the function.

def cache(func):
    cache_value = {}
    print("hello",cache_value)                      # For first call only   
    def wrapper(*args):
        print("hello",cache_value)                      # For each call
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b

print(long_running_function(2,3))
print(long_running_function(4,7))
print(long_running_function(2,3))