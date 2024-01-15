list1 = [10,501,22,37,100,999,87,351]
list2 = [10,501,22,37,100,999,87,351]
for i in list1[:]:
    if(i%2!=0):
        list1.remove(i)
print(list1)
for i in list2[:]:
        if(i%2==0):
            list2.remove(i)
print(list2)