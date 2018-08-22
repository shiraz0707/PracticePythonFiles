# www.practicepython.org - Exercise 4
'''This program asks a number from the user and prints
the divisors of that number'''

num = int(input("Please enter the number to divide: "))

'''this creates a list from 1 to entered number and put values
increment of 1 until the list reaches the entered value
ex: if you enter 9, it will create a list having
1,2,3,4,5,6,7,8,9
'''
listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)