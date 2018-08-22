def fibonacci(number):
	x = 0
	y = 1
	for i in range(0,number):
		f = x + y
		print(f)
		x = y
		y = f

userNumber = int(input('how many fibonacci numbers? '))
fibonacci(userNumber)