"""
Here we start our journey to the world of JSON stands for JavaScript Object Notation:
• It's a lightweight way to save and exchange data through different platforms
• JSON has the same notation as the dictionaries on Python
• The variables in JSON are like Python but in this case we have
    Python        JSON
    ---------------------
    dict -> Object
    int,long, float -> Numbers
    string -> String
    None -> Null
    Lists -> Array
    Tuples -> Array
{
    name: "Danilo"
    age: 21
    surname: "Quattrini"
}
"""

# First, we import the library that it's necessary to work with JSON file
import json
"""
Serialization: is the process to convert a value from one format to the other one,
in this case we want to pass the value of an int inside the json file.

JSON have this function call dump(), where we convert the values from a Python format
to a JSON one.
"""
x = 10
print(json.dumps(x))

"""
It's important to consider the context manager for file handling.
Why that? In first place when we open a file, we need to close it, after 
its usage, in that way we avoid any types of leaks and issues.

Python has a built-in functionality to handel this problem,
its name is context manager, where we can use the keyword

with open(<file>, <rule>) as f

we can read its context safely and 
This eliminates need to explicitly call close() and 
protects against resource leakage in case of unexpected failures.
"""

# 1.0 Here we read the context of the file "text.txt"
with open("text.txt", "r") as f:
    data = f.read()
    print(data)

# 2.0 Here we write the context of the file "text.txt"
with open("text.txt", "w") as f:
    data = "sono il dato nuovo"
    f.write(data)

var = {
    # This is an object, like in java that contains other variables
    "Subjects": {
        "Math": 85,
        "Physics": 100
    }
}

# 3.0 now we use the context manager to write the content of var
with open("sample.json", "w") as f:
    json.dump(var, f)

"""
Deserialization

It's the opposite process of the serialization, where here, we 
convert the datas from the JSON file and save them into a 
python variable.

we use the json.load() function to do this operation 
"""
with open("sample.json", "r") as read_j:
    data = json.load(read_j)