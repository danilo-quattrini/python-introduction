'''
In this script we start to use our first statements:

• if <condition>:
        <do-something>
    else
        <do-something-else>

• while <condition>:
    <code-here>

• for <element> in <list>:
    print(element)

'''

# easy if statement for this scope
a = 16
b = 15
if a < b:
    print("a minor of b")
else:
    print("a bigger than b")

# EX 1: print all the numbers from 1 to 10 with for cicle
# this is with a list
number = [1,2,3,4,5,6,7,8,9,10]
for i in number:
    print(i)
# without the list we use the function range(<start>, <stop> - 1)
# range(start, stop, step): Generates numbers from start to stop-1, incrementing by step.
for i in range(0, 11, 2):
    print(i)

# EX 2: print all the even numbers from 1 to 50
for i in range(1, 50):
    if i % 2 == 0 : print(i)

# EX 3: from a list we print all the number that are greater than 10
numbers_list = [1, 56,6 ,62, 26, 10, 11, 12]
for i in numbers_list:
    if i > 10: print(i)

'''
EX 4: ask to the user the input for a variable
	•	if it's bigger than 100 print “Grande”,
	•	if it's within 50 e 100 print “Medio”,
	•	altrimenti stampa “Piccolo”
'''
a = int(input("Insert the numb you want to check"))
if a >= 100:
    print("Big")
if 100 > a >= 50:
    print("Mid")
if a < 50:
    print("Small")

# EX 9 use the while statement to print all the numbers backward from the list number
i = 1
while i < len(number):
    print(number[-i]) # We can move through the list backward from -1 to -len() to simulate the revers
    i = i + 1

# EX 10 use the list number with the for statement to simulate the sum function
numbers_sum = 0
for i in number:
    numbers_sum += i
print(numbers_sum)
