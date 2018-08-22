# www.practicepython.org - Exercise 2 Extra 1
import random

#compute random lists

# Create two empty lists
List_a = []
List_b = []

# Create the first list with random numbers using randint function
for x in range(0,20):
    a = random.randint(0,20)
    List_a.append(a)

# Create the second list with random numbers using randint function
for y in range(0,20):
    b = random.randint(0,20)
    List_b.append(b)

#To see how the randomly generated list looks like
print ('List_a:',List_a)
print ('List_b:',List_b)


#remove duplicates on the random lists
rand_a = set(List_a)
rand_b = set(List_b)

#To see how the randomly generated list looks like after removing duplicates
print ('List_a:',rand_a)
print ('List_b:',rand_b)

#compare the two random lists (random lists that the duplicates are removed)
commonList = []
for number in rand_a:
    if (number in rand_b) == True:
        commonList.append(number)
        print number
print (commonList)