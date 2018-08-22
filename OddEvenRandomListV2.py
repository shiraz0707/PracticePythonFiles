import random

numlist = []
# gives a random number between 5 and 15
list_length = random.randint(5,15)

print list_length

# The length of the numlist increases everytime a random number is added
while len(numlist) < list_length:
    numlist.append(random.randint(1,75))
    

evenlist = [number for number in numlist if number % 2 == 0] 

print(numlist)
print(evenlist)