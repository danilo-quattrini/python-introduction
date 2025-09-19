"""
    Author: Danilo Quattrini
    Date: 19-09-2025

    Python Data Types script to practise how to use the variables inside the code.

    We know that in Python we don't have to declare the types of our data, we just need
    to assign them.
    These are a set of exercises from the course 30 days of python with
    Asabhen, for more info, read the README file.
"""
from math import remainder

## These are string variables, we can use them to save string datas.
first_name = "Danilo"
last_name = "Quattrini"

## We can concatenate two different strings
full_name = first_name + " " + last_name
country = "Italy"
city = "Milan"

## That's our int variable, we can convert into a string with the function str()
age = 22
year = 2025

## First bool variable we declare, we can use only True or False
is_married = False
is_true = True
is_light_on = False

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)

## Declare multiple variables in one line

pc_name, os_system, gb_ram = "MacBook Pro M2", "Tahoe", 16

"""
    In the second part of this script I'm going to use some built-in function,
    to see how these variable are saved inside the system, for instance I'm 
    use the type() function to see the type of variable. 
"""

## That would be a string
print(type(first_name), type(age), type(is_married))

## With len() we see the length of the string in this case first_name it would be 6 characters length
print(len(first_name))

## We can compre the length of these strings
print(len(first_name) != len(last_name))

## We can make some operation with our variables
num_one = 5
num_two = 4

total = num_one + num_two
subtraction = num_one - num_two
division = num_one / num_two
module = num_one % num_two
reminder = num_one // num_two

print('Addition:', num_one, '+', num_two, '=', total)
print('Subtraction:', num_one, '-', num_two, '=', subtraction)
print('Division:', num_one, '/', num_two, '=', division)
print('Modulus:', num_one, '%', num_two, '=', module)
print('Floor division:', num_one, '//', num_two, '=', reminder)
