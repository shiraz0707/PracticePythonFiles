import random
print sorted([number for number in random.sample(range(1,500),20) if number % 2 == 0])