def dec_to_bin(decNum):
	binNum =bin(decNum)
	return binNum

def dec_to_oct(decNum):
	octNum=oct(decNum)
	return octNum

def dec_to_hex(decNum):
	hexNum=hex(decNum)
	return hexNum

decNum=int(input('please enter decimal number: '))

print dec_to_bin(decNum)[2:]
print dec_to_oct(decNum)[1:]
print dec_to_hex(decNum)[2:]


#dec_to_bin(decNum)
#dec_to_oct(decNum)
#dec_to_hex(decNum)
#print binNum
#print octNum
#print hexNum