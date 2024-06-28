# iteratable - iter



# # 1. Counting Positive Numbers
# #       {   Given list of numbers, count how many are positive    }

# num_list = list(map(int, input("Enter the values of list: ").split(", ")))
# positive_count = 0
# for num in num_list:
#     if (num>0):
#         positive_count+=1
# print("Number of positive numbers is", positive_count)



# # 2. Sum of Even Numbers
# #       {   Calculate the sum of even numbers up to a given number 'n'    }

# num = int(input("Enter the number: "))
# sum_even = 0
# for i in range (2, num+1, 2):
#     sum_even += i
# print("Sum of all the even numbers up to", num, "is", sum_even)



# # 3. Mulptiplication Table Printer
# #       { run iteration till 10, but skip the 5th iteration }

# num = int(input("Enter the number for which multiplication table need to be printed: "))
# for i in range(1,11):
#     if (i==5):
#         continue
#     print(num, "*", i, "=", num*i)



# # 4. Reverse a string
# #       { using loop }

# str = input("Enter the string: ")
# reverse_str = ""
# str_len = len(str)
# for i in range(str_len-1,-1,-1):
#     reverse_str += str[i]
#     # print(str[i], end="")
# print(reverse_str)



# # 5. Find the First Non-Reapeated character.
# #       {   Given a string, find the first non-repeated character   }

# str = input('Enter the string: ')
# for char in str:
#     if (str.count(char) == 1):
#         print(char)
#         break



# # 6. Factorial Calculator
# #       {   Compute the factorial of a number using a while loop.   }

# num = int(input('Enter the number to calculate the factorial: '))
# i = 2
# result = 1
# while (i<=num):
#     result *= i
#     i+=1
# fact_statement = "The factorial of {} is {}."
# print(fact_statement.format(num,result))



# # 7. Validate Input
# #       {   Keep asking the user for the input until they enter a number between 1 and 10.     }

# num = int(input("Enter the number: "))
# while not(1 <= num <= 10):
#     print("Please enter a valid number, between 1 and 10.")
#     num = int(input("Enter the number: "))
# print("You entered a valid number {}.".format(num))



# # 8. Prime Number Checker           -       Greater than 1
# #       {   Check if the number is prime.   }

# num = int(input("Enter the number for prime check: "))
# prime = 1
# for i in range(2,num):
#     if not(num%i):
#         print("The number is not prime.")
#         prime = 0
#         break
# if (prime):
#     print("The number is prime.")



# # 9. List Uniqueness Checker
# #       {   Cheak if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.  }

# unique_list = list(input("Enter the values of list: ").split(", "))
# duplicate = False
# for i in unique_list:
#     if (unique_list.count(i) != 1):
#         print(i)
#         duplicate = True
#         break
# if not(duplicate):
#     print("List contain all unique values.")

# unique_list = list(input("Enter the values of list: ").split(", "))
# unique_set = set()
# for i in unique_list:
#     if i in unique_set:
#         print(i)
#         break
#     unique_set.add(i)



###############################################################################################

# # 10. Exponential Backoff
# #       {   Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.    }

# import time

# wait_time = 1
# max_retries = 5
# attempts = 0

# while (attempts < max_retries):
#     print("Attempt", attempts+1, "wait time", wait_time, "seconds")
#     time.sleep(wait_time)
#     wait_time *= 2
#     attempts += 1 