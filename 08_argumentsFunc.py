# There are four types of arguments in functions
# 01. Default arguments
# 02. Keyword arguments
# 03. Required arguments
# 04. Variable length arguments

# 01
# def average(a=9,b=1):
#     print("The average is : ", (a+b)/2)
# average()
# average(4,4)
# average(5)
# average(b=9)

# 02
# def average(a=9,b=1):
#     print("The average is : ", (a+b)/2)
# average(b=9,a=21)

# 03
# def average(a,b,c=1):
#     print("The average is : ", (a+b+c)/2)
# average(9,10,11)

# 04 (a) tuple
# def average(*numbers):  
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print( "Average is : ", sum/len(numbers) )
# average(5,6)
# average(4,5,6)
# average(2,8,9,1)

# (b) dictionary
# def name(**name):
#     print(type(name))
#     print( "Hello",name["fname"] ,name["mname"] ,name["lname"] )

# name(fname="Anil",mname="Kumar",lname="Jindal")