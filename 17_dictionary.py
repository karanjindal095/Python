''' 01 '''
dic = {
    "name" : "karan",
    "object": "spoon",
    500: "ram",
    600:"shyam",
    700:'rohan'
}
# print(dic)
# print(type(dic))
# print(dic["name"])
# print(dic[500],dic[700])

# ''' 02 '''
# info = {'name':'karan','age':19,"eligible":True}
# print(info)
# print(info["name"])       #gives error if name is not present in dict
# print(info.get("name"))   #don't give error if name is not present in dict

''' 03 keys() = 'keys are the names' and values() = 'values are the values of keys' '''
info = {'name':'karan','age':19,"eligible":True}
# print(info.keys())
# print(info.values())

# for i in info.keys():
#     print(info[i])

# for key in info.keys():
#     print(f"the value of key {key} is {info[key]}")

''' 04 items() = 'it will print both keys and values ' '''
# info = {'name':'karan','age':19,"eligible":True}
# print(info.items())
# print(type(info.items()))
# for key,value in info.items():
#     print(f"the value of {key} is {value}")