# www.practicepython.org - Exercise 6
word = raw_input("Enter word:")

if word == word[::-1]:
	print ('The word',word,'is a palindrome')
else:
	print ('The word',word,'is NOT a palindrome')