'''01 without enumeration'''
# l = [11,12,13,14,15,16]
# print(l)
# index = 0
# for i in l:
#     print(i)
#     if(index == 3):
#         print("index 3 ")
#     index += 1
    
''' 02 enumeration'''
# marks = [11,12,13,14,15,16]
# for index, i in enumerate(marks):
#     print(i)
#     if(index==3):
#         print("index 3")

'''03'''
# fruit = ["mango","apple","banana","orange"]
# for index,i in enumerate(fruit):
#     print(index,i)
# print(type(i))

''' prints tuple (0, 'mango')'''
# fruit = ["mango","apple","banana","orange"]
# for i in enumerate(fruit):
#     print(i)
# print(type(i))

'''start=1 : we can change index count'''
# fruit = ["mango","apple","banana","orange"]
# for i in enumerate(fruit,start=1):
#     print(i)
# print(type(i))