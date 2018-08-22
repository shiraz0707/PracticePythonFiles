# This converts decimal to binary
def Decimal_To_Binary(dec_number):	
	binary_list=[]
	while (dec_number>0):
	    a=dec_number%2
	    binary_list.append(a)
	    dec_number=dec_number/2

	string =""
	for j in binary_list[::-1]:
	    string=string+str(j)
	return string
	    
dec_number=int(input('Enter the decimal number: '))

binValue = Decimal_To_Binary(dec_number)
print binValue


'''
binary = raw_input('enter a binary number: ')
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print decimal
'''