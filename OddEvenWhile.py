# www.practicepython.org - Exercise 2

num= int(input("Enter number:"))
while num!=0:
	if num % 2 == 0:
		print(str(num) + " is an even number")
	else:	
		print(str(num) + " is an odd number")
	num= int(input("Enter number:"))
## modify the above 