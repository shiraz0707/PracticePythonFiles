'''
Program name: listLessThanFive.py
Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
'''
'''Extras:
1. Instead of printing the elements one by one, make a new list that has all the elements 
less than 5 from this list in it and print out this new list.
WARNING: CAREFUL WHERE YOU PLACE THE INCREMENTAL COUNT

2. Write this in one line of Python.

3. Ask the user for a number and return a list that contains only elements from 
the original list a that are smaller than that number given by the user.
'''

# www.practicepython.org - Exercise 3


## Original Program
'''
my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
i=0

while my_list[i] !=0:
	if my_list[i] < 5:
	   print(my_list[i])
	   i=i+1
'''

# Extra 1
'''
my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = [ ]
i=0

while i < len(my_list):
	if my_list[i] < 5:
	  	new_list.append(my_list[i])
	i+= 1
print new_list
'''

# Extra 3
number= int(input("Enter number:"))
my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = [ ]
i=0

while i < len(my_list):
	if my_list[i] < number:
	  	new_list.append(my_list[i])
	i+= 1
print new_list