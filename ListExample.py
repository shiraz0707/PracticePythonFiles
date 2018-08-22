numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
#adding the numbers to the numbers list
numbers.append(1)
numbers.append(2)
numbers.append(3)

#adding the 'hello' and 'world' to the strings list
strings.append("hello")
strings.append("world")

second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
raw_input("\n\nPress the enter key to exit.")