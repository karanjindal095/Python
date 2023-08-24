'''  01
# printing Lists '''

marks = [3,5,6,"Karan",True]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
''' negative indexing'''
# print(marks[-2])
# print(len(marks))
# print(marks[len(marks)-2])

'''  02
# check whether an item is present in list?'''

# if 7 in marks:
#     print("yes")
# else:
#     print("no")

# if "Karan" in marks:
#     print("get it")
# else:
#     print("no")

# if "kar" in "karan":
#     print("yea")
# else:
#     print("nope")

'''  03
# printing elements in a particular " RANGE " '''

# mark1 = [3,5,6,"Karan",True,145,15,12,36,50]
# print(mark1[:])
# print(mark1[:10])
# print(mark1[1:9])
# print(mark1[1:9:2])

'''  04
# List comprehension '''

# lst = [i for i in range(10)]
# print(lst)
# lst = [i*i for i in range(1,10)]
# print(lst)
# lst = [i for i in range(10) if i%2==0]
# print(lst)
# lst = [i for i in range(50) if i%3!=0]
# print(lst)

'''checks elements are equal or not index wise'''
# list1 = [1, 2, 3, 4]
# list2 = [1, 9, 3, 8]
# result = []
# for i in range(len(list1)):
#     result.append(list1[i] == list2[i])

# print(result)

# comparing list elements
# l=[10,20,30]
# l1=[2]
# for x in l:
#     for y in l1:
#         if x==y:
#             print("true")
#         else:
#             print("false")
    
# list1 = [1, 2, 3, 4]
# list2 = [1, 9, 3, 8]
# result = []
# for i in range(4):
#     result.append(list1[i] == list2[i])