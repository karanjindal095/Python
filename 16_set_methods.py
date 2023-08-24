'''01 union() and update() '''
# s1 = {1,2,5,6}
# s2 = {3,6,7}
# print(s1.union(s2))
# print(s1,s2)
'''02 '''
# s1.update(s2)
# print(s1,s2)

'''03 intersection() and intersection_update() '''
# state = {"punjab","haryana","up","hyderabad"}
# state1 = {"delhi","punjab","up","mumbai"}
# state2 = state.intersection(state1)
# print(state2)
'''04 '''
# state.intersection_update(state1)
# print(state)

'''05 symmetric_difference() and symmetric_difference_update() '''
# state = {"punjab","haryana","up","hyderabad"}
# state1 = {"delhi","punjab","up","mumbai"}
# state2 = state.symmetric_difference(state1)
# print(state2)
'''06 '''
# state.symmetric_difference_update(state1)
# print(state)

'''07 difference() and difference_update()'''
# state = {"punjab","haryana","up","hyderabad"}
# state1 = {"delhi","punjab","up","mumbai"}
# state2 = state.difference(state1)
# print(state2)
'''08 '''
# state.difference_update(state1)
# print(state,state1)

'''09 isdisjoint()'''
# a = {1,2,3,4}
# b = {5,6,7,8}
# print(a.isdisjoint(b))
# c = {7,8,9,1}
# print(a.isdisjoint(c))

'''10 issuperset()'''
# a = {1,2,3,4,5,6,7,8}
# b = {1,2,3,4}
# print(a.issuperset(b))
# c = {1,2,9}
# print(a.issuperset(c))

'''11 issubset()'''
# a = {1,2,3,4,5,6,7,8}
# b = {1,2,3,4}
# print(b.issubset(a))
# c = {1,2,9}
# print(c.issubset(a))

'''12 add()'''
# state = {"punjab","haryana","up","hyderabad"}
# state.add("kerela")
# print(state)

'''13 remove()/discard()'''
# state = {"punjab","haryana","up","hyderabad"}
# state.remove("up")
# # state.remove("mp")           #ERROR
# state.discard("haryana")
# state.discard("gujarat")
# print(state)

'''14 pop()'''
# state = {"punjab","haryana","up","hyderabad"}
# print(state.pop())

'''15 clear()'''
# state = {"punjab","haryana","up","hyderabad"}
# state.clear()
# print(state)
