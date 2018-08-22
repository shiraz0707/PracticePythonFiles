'''
This program creates a random list and extract the even and odd numbers 
and put into the respective lists
'''
import random

rand_list = [random.randrange(1,101,1) for i in range(10)]
even_list = [e for e in rand_list if e%2 == 0]
odd_list = [o for o in rand_list if o%2 != 0]

print "Odd and Even numbers:	", rand_list	
print "Even numbers:	", even_list
print "Odd Numbers:	", odd_list