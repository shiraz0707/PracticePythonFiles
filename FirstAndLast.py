'''
Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only 
the first and last elements of the given list.
Python Practice - Exercise 12 solution
'''

def getFirstLast (my_list):
	return [my_list[0], my_list[len(my_list)-1]]
	
my_list=[x for x in range(5,51,5)]
print getFirstLast(my_list)

# You can use the following instead of 11 and 12
#print getFirstLast([x for x in range(5,51,5)])