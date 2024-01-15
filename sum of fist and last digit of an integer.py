'''write a python program to find the sum of fist and last digit of an integer'''

num = int(input("enter the integer number"))
last = num%10
while num!=0:
    first = num%10
    num = num//10
sum = last + first
print("sum of first and last digit is : ", sum)