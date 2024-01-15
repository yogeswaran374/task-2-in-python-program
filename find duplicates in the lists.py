'''find duplicates in the three lists'''
list1 = []
list2 = []
list3 = []

for i in range(5):
    list1.append(i)
print(list1)
for i in range(3,7):
    list2.append(i)
print(list2)
for i in range(5,8):
    list3.append(i)
print(list3)
list1.extend(list2)
print(list1)
list1.extend(list3)
print(list1)
dup=[]
unique = []
for i in list1:
    if i not in unique:
        unique.append(i)
    elif i not in dup:
        dup.append(i)
print(dup)


