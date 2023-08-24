'''  f - string  ''' 
a = "Hey my name is {} and i am from {}"
name = "Karan"
country = "India"
# print(1,a)
# print(2,a.format(name,country))
print(3,f"Hey my name is {name} and i am from {country}")
# print(4,f"Hey my name is {{name}} and i am from {{country}}")
# b = f"Hey my name is {name} and i am from {country}"
# print(5,b)
price = 80.5982
c = f"dollar price is {price: .2f}"
print(6,c)

'''  doc - string  '''

# def name(a):
#     '''hello enter the name'''
#     print(a)
# name("karan")
# print(name.__doc__)

# def square(n):
#     '''takes a no. and return the square of it'''
#     print(n**2)
# square(5)
# print(square.__doc__)