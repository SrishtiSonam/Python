# # 1. Age Group Categorization
# #       Classify a person's age group: Child (<13), Teenager(13-19), Adult(20-59), Senior (60+)

# age = int(input("Enter your age: "))
# group = ''
# if (age < 13):
#     group = "child"
# elif (age <=19 ):
#     group = "teenager"
# elif (age <=59):
#     group = "adult"
# else:
#     group = "senior"
# statement = "You are a {}."
# print(statement.format(group))



# # 2. Movie Ticket Pricing
# #       Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

# age = int(input('Enter age: '))
# isWednesday = bool(input('Is it wednesday: (1 for yes / 0 for no)   '))
# cost = 12 if age>=18 else 8                       # *************************** #
# if (isWednesday):
#     discount = 2
#     cost=-discount
# order_statement = "Your amount to be paid is ${}."
# print(order_statement.format(cost))



# # 3. Grade Calculator
# #       Assign a letter grade on the basis of score: A(100-90), B(89-80), C(79-70), D(69-60), F(below 60)

# score = int(input("Enter your marks, out of 100: "))
# if (score>=0 and score<=100):
#     grade = ''
#     if (score>=90):
#         grade = 'A'
#     elif (score>=80):
#         grade = 'B'
#     elif (score>=70):
#         grade = 'C'
#     elif (score>=60):
#         grade = 'D'
#     else:
#         grade = 'F'
#     grade_statement = "Your grade is \'{}\' for marks {}."
#     print(grade_statement.format(grade, score))        
# else:
#     print("Enter valid marks for grade calculation.")



# # 4. Fruit Ripeness Checker
# #       Determine if a fruit is ripe, overripe, or unripe based on its color. 
# #           (eg. Banana: Green-Unripe, Yellow-Ripe, Brown-Overripe  )

# fruit = input("Enter the name of the fruit: ")
# print(" \'G\' for green, \'Y\' for yellow, \'B\' for brown")
# color = input("Enter the color of fruit: ")
# if (not((color == 'G') or (color == 'Y') or (color == 'B'))):
#     print("Enter valid color.")
#     exit()
# status = ""
# if (color == 'G'):
#     status = "unripe"
# elif (color == 'Y'):
#     status = "ripe"
# elif (color == 'B'):
#     status = "overripe"
# status_statement = "{} fruit with color '{}' is {}."
# print(status_statement.format(fruit,color,status))



# # 5. Weather activity suggestions
# #       Suggest an activity based on weather. 
# #           (e.g. Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snownam.)

# print("Enter \'S\' for sunny, \'R\' for rainy, \'S\' for snowy")
# weather = input("Enter the weather condition: ")
# W = ['S', 'R', 'S']
# if (weather not in W):
#     print("Enter a valid weather code.")
#     exit()
# if (weather == W[0]):
#     print("Go for a walk.")
# elif (weather == W[1]):
#     print("Read a book.")
# elif (weather == W[2]):
#     print("Build a snowman.")



# 6. Transportation Mode Selection
# #       Choose a mode of transportation based on the distance 
# #           (eg: <3km:Walk, 3-15km:Bike, >15km:Car)

# dist = float(input("Enter the distance (in km): "))
# if (dist<3.0):
#     mode = "walk"
# elif (dist<=15.0):
#     mode = "bike"
# else:
#     mode = "car"
# mode_statement = "As the distance is {}km, so mode of transportation should be {}."
# print(mode_statement.format(dist, mode))



# # 7. Coffee Customization
# #       Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot of espresso"

# print("Coffee : \'Small\', \'Medium\', \'Large\' '")
# size = input("Enter the coffee size: ")
# order_size = size.lower()
# size_available = ['small', 'medium', 'large']
# if order_size not in size_available:
#     print("Enter a valid size.")
#     exit()
# extra_shot = bool(int(input("Do you want extra shot of espresso. (1 for \'yes\' or  0 for \'no\'): ")))
# extra_shot_of_espresso = "with" if extra_shot else "without"
# coffee_order_statement = "One {} cup of coffee {} extra shot of espresso."
# print(coffee_order_statement.format(order_size,extra_shot_of_espresso))



# # 8. Password Strength Checker
# #       Check if a password is "Weak", "Medium", or "Strong".
# #           Criteria: <6chars (Weak), 6-10chars(Medium), >10chars(Strong)
# password = input("Enter the password: ")
# pass_len = len(password)
# if (pass_len < 6):
#     criteria = "weak"
# elif (pass_len <= 10):
#     criteria = "medium"
# else:
#     criteria = "strong"
# password_statement = "Your password \"{}\", is a {} password in terms of strength."
# print(password_statement.format(password, criteria))


# # 9. Leap Year Checker
# #       Divisible by 4, but not by 100 unless also divisible by 400.
# year = int(input("Enter the year for leap_year_check: "))
# if ( ( (year%4)==0 and (year%100)!=0 ) or ( (year%400)==0 ) ):
#     print("A leap year.")
# else:
#     print("Not a leap year.")



# 10. Pet Food Recommendation
#       Recommend a type of food based on the pet's species and age.
#           (e.g. Dog: < 2years - Puppy food, Cat: > 5years - Senior cat food)