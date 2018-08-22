# www.practicepython.org - Exercise 5

fibonacci_list = [1,1,2,3,5,8,13,21,34,55,89]
normal_list = list(range(1,13))
common_list=[]
i=0

print('fibonacci list has :',fibonacci_list)
print('normal list has : ',normal_list)

for i in range(len(fibonacci_list)):
	if fibonacci_list[i] in normal_list and fibonacci_list[i] not in common_list:
		common_list.append(fibonacci_list[i])
		
print ('The common list has :', common_list)	