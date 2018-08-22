'''
Write a program (function!) that takes a list and returns a new list that 
contains all the elements of the first list minus all the duplicates.
Practice Python - Exercise 14 (No extras done)
'''

def create_unique_list(number_of_elements):
	num_list=[]
	for x in range(0,number_of_elements):
		number = random.randint(0,number_of_elements)
		num_list.append(number)
	print num_list
	num_list=set(num_list)
	num_list=list(num_list)
	
	return num_list


import random

number_of_elements = int(input('Enter the number of elements of the list: '))
print create_unique_list(number_of_elements)