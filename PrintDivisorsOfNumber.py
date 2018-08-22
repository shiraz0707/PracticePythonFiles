''' Print the list of divisors for a given number'''
num = int(input("Enter the number to find the divisors: "))

list_range = list(range(1,num+1))
divisor_list=[]

#print list_range

for number in list_range:
	if num%number==0:
		divisor_list.append(number)
print(divisor_list)

