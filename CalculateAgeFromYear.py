# Practice Python - Exercise 7 example
import datetime
# without using List Comprehension
'''
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = []
for year in years_of_birth: 
	ages.append(2014 - year)
print ages
'''
# This gives the current date in yyyy-mm-dd format
today = datetime.date.today()

# This gives only the year
currentyear = datetime.date.today().year

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]

# with using List Comprehension
#Calculates the ages based on the current year and the years of birth list
ages = [(datetime.date.today().year) - year for year in years_of_birth]

print ages