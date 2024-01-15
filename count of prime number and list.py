
'''count of prime numbers from the given list'''


list = [10,501,22,37,100,999,87,351]
count = 0
for i in list[:]:
    if(i%2==0):
        list.remove(i)
print("the list of prime numbers :", list)
print("the count of prime numbers from the list", len(list))

