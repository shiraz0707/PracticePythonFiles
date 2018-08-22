'''
Write a program (using functions!) that asks the user for a long string 
containing multiple words. Print back to the user the same string, 
except with the words in backwards order
Practice Python - Exercise 15
'''

def reverse_string(string):
	result = string.split()[::-1]
	st_rev = ' '
	for i in result[::-1]:
		st_rev = i + ' ' + st_rev
	return st_rev

string = raw_input("Enter the string sentence you want to reverse: ")
print reverse_string(string)