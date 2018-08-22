div_list=[]
number = int(input("Enter number:"))
original_number=number
result=0

while (number%2==0):
	result=number/2
	div_list.append(result)
	number=result
	if (2 in div_list)==0:
		div_list.append(2)

while (number%3==0):
	result=number/3
	div_list.append(result)
	number=result
	if (3 in div_list)==0:
		div_list.append(3)

while (number%5==0):
	result=number/5
	div_list.append(result)
	number=result
	if (5 in div_list)==0:
		div_list.append(5)

while (number%7==0):
	result=number/7
	div_list.append(result)
	number=result
	if (7 in div_list)==0:
		div_list.append(7)


div_list.append(original_number)
print div_list