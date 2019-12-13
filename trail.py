import copy
li1 = [3,5,6,7,8]

li2 = copy.copy(li1)

print('li1 = ',li1)
print('li2 = ',li2)

li1[3]=234


print('li1 = ',li1)
print('li2 = ',li2)