import random

rand_list = [random.randrange(1,101,1) for i in range(10)]

# Unsorted
print rand_list
# sorted

print (sorted(rand_list))

# Unsorted

print [e for e in rand_list if e%2 == 0]

# sorted

print sorted(e for e in rand_list if e%2 == 0)
