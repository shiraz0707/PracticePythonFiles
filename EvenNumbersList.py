# Practice Python - Exercise 7

# My solution
'''mylist=[x*x for x in range(1,11)]
newlist=[]

print mylist

for i in range(len(mylist)):
	if mylist[i] % 2 == 0:
		newlist.append(mylist[i])
print newlist
'''

# Michele solution 

mylist=[x*x for x in range(1,11)]

print [element for element in mylist if element % 2 == 0]

#print newlist
