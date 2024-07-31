file_1 = open('01_enumerate.py')                    # Opening the file and giving the reference 

file_2 = open('test.txt', 'w')                       # file will be created, if not there.
try:
    file_2.write('Hello!! \n Chai aur Code.')
finally:
    file_2.close()


# Here no need to close, automatically handled here.
# 'try', 'finally' are not required here.
with open('test.txt', 'w') as file:
    file.write('\nChai aur Python.')