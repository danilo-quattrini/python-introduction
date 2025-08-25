"""
We start to define our first function:

def <name-function>(<value>)
    return f "Hello<value>"
• def -> we say to python that we are defining a function
• () -> where we insert the value that we want to insert inside the function
• <name-function> -> this is the name we use to refer to the function we want to use
• return <something> -> we return the value

"""
# 0.0 First function where we don't pass the arguments inside it
def hello():
    print("Hello, World!")
hello()

# 1.0 We start to use the print
def say_hy(world_print = "Pippo"):
    return f"Hello, {world_print}"

help(say_hy)
print(say_hy())

# 2.0 We pass the parameter that we insert in input before
def sum_numbers(x, y):
    """The sum of two numbers passed with parameters"""
    return x + y # Return the values from a function

a = int(input("Insert the value of a: "))
b =  int(input("Insert the value of b: "))
result = sum_numbers(a, b)
print(f"The result of the sum of {a} and {b} is {result}")

'''
3.0 Scope where we know that outside the variable doesn't exists
inside the function we cannot see 
'''
x = 10
def test(x):
    x = 5
    return x
print(test(x))
print(x)