'''This program simply takes the name and the age as input and displays 
message saying something like Hey, so and so, you will be 100 years old 
when you in year XXXX'''
# www.practicepython.org - Exercise 1

'''import datetime

my_name = raw_input("Enter name: ")
age = int(input("Enter age: "))

now = datetime.datetime.now()
current_year=now.year

count = 100-age
year_to_100 = current_year + count

print "Hey %s, you will be 100 years in year %d" % (my_name,year_to_100) 
'''

import datetime

my_name = raw_input("Enter name: ")
age = int(input("Enter age: "))

# Gives the current date and time 
now = datetime.datetime.now()

count = 100-age

year_to_100 = now.year + count

print "Hey %s, you will be 100 years in year %d" % (my_name,year_to_100) 