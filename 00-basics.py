"""
This is a variable that can save every type of value
form: int, char, float, bool, string, lists and
dict

!! NOTE: we don't need to declare them before
the type of variable, Python understands which variable you need
in that exact moment
"""

a = 10
b = 10.645
c = "Hy my name is danilo, how are you"
d = True
e = [a, b, c, d] # Lists can contain every type of variable
print(e) # print(<variable>), we print our first list

# EX 1: Create a variable with my name, age, city and print them
name = "Danilo"
age = 22
city = "Civitanova Marche"
print("This is my name", name ,"This is my age", age,"This is my city town", city)

'''
EX 2: Create a list of 7 numbers and prin:
    • The first number
    • The last number
    • The length of the list 
'''
my_list = [1,3,5,6,2,6,8]
print(my_list[0])
print(my_list[-1])
print(len(my_list))
print(my_list[1:])
'''
dict: they are dictionaries where you can correlate the key to its value

dict: <key>:<value>
'''
my_dict = {"name": "Danilo", "surname": "Quattrini", "age": 22}
print(my_dict) # print the values inside the dicy, they are pairs of <key>:<value>
# now we say get the value with the key that's inside the function .get()
# module.get(<key>)
print(my_dict.get("name"), my_dict.get("surname"), my_dict.get("age"))


# EX 3: Create a dictionary where we represent a book with the keys of: title, author, year
book = {"title":"Harry Potter", "author":"J.K Rowling", "year": "2020"}
print(book.get("author"))

'''
EX 4: Take the exercises n°2 and do these calculation:
    • sum
    • max
    • min
    • average
'''
print("Sum:", sum(my_list))
print("Max:",max(my_list))
print("Min:",min(my_list))
print("Avg:",sum(my_list) / len(my_list))
