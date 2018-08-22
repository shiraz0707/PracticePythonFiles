'''
Write a program that asks the user how many Fibonnaci numbers to 
generate and then generates them
'''

def create_fibonacci(last_number):
	#fibo_list = [0, 1]
	for i in range(2,last_number):
		fibo_list.append(fibo_list[i-1]+fibo_list[i-2])
	return fibo_list

last_number=int(input('Enter the number to create fibonacci: '))

fibo_list = [0, 1]
print create_fibonacci(last_number)