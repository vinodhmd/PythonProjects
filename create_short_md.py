import os

posts = [
    {
        "title": "Variables & Data Types",
        "desc": "Python makes variable assignment incredibly simple. No types needed!",
        "code": '''name = "Vinodh"       # String
age = 45              # Integer
height = 5.9          # Float
is_student = False    # Boolean

print(f"{name} is {age} years old.")'''
    },
    {
        "title": "Typecasting",
        "desc": "Need to convert datatypes? Python provides built-in functions to safely convert values on the fly.",
        "code": '''age = "45"           # Currently a string
age = int(age)       # Converted to Integer!

is_active = bool(1)  # Evaluates to True
pi = str(3.14159)    # Converted to String "3.14159"'''
    },
    {
        "title": "Math Operators",
        "desc": "Basic arithmetic is straightforward, and the built-in 'math' module handles the complex stuff seamlessly!",
        "code": '''import math

# Simple Operators
x = 10 + 5       # 15
y = 10 ** 2      # Exponent (100)
z = 10 // 3      # Floor division (3)

# Math Module
area = math.pi * (5 ** 2)
print(math.floor(3.7)) # Rounds down to 3'''
    },
    {
        "title": "Conditional Statements",
        "desc": "Control the flow of your program cleanly with if, elif, and else blocks. Python relies on indentation for this!",
        "code": '''age = 20

if age >= 18:
    print("Eligible to vote!")
elif age < 0:
    print("Invalid age!")
else:
    print("Underage.")'''
    },
    {
        "title": "F-Strings Magic",
        "desc": "Introduced in Python 3.6, f-strings are the most readable way to format text dynamically.",
        "code": '''name = "Vinodh"
score = 95.5

# Clean, readable, and fast text formatting!
print(f"Hello {name}! You scored {score}%.")

# You can even evaluate math or logic directly inside them:
print(f"Next year you will be {2026 - 1980} years old.")'''
    },
    {
        "title": "String Methods",
        "desc": "Python has incredibly powerful built-in methods to manipulate text in a single line.",
        "code": '''text = "  python programming  "

print(text.strip())            # "python programming"
print(text.upper())            # "PYTHON PROGRAMMING"
print(text.title())            # "  Python Programming  "
print(text.replace("o", "a"))  # "  pythan pragramming  "'''
    },
    {
        "title": "Lists (Arrays)",
        "desc": "Lists are ordered, changeable, and allow duplicate values. The go-to collection in Python!",
        "code": '''fruits = ["apple", "banana", "cherry"]

fruits.append("orange")    # Add item to the end
fruits.insert(1, "kiwi")   # Insert at a specific index
removed = fruits.pop()     # Remove & return the last item

print(fruits[0:2])         # Slicing: ['apple', 'kiwi']'''
    },
    {
        "title": "Dictionaries",
        "desc": "Dictionaries store data in Key-Value pairs, allowing for extremely fast lookups!",
        "code": '''user = {
    "name": "Vinodh",
    "role": "Developer",
    "active": True
}

print(user.get("name"))    # Safe access: "Vinodh"
user["country"] = "India"  # Add a new key-value pair

for key, val in user.items():
    print(f"{key}: {val}")'''
    },
    {
        "title": "Tuples & Sets",
        "desc": "Tuples are immutable (cannot be changed). Sets hold unordered UNIQUE items.",
        "code": '''# Tuple () - Faster than lists and protects data from modification!
coordinates = (10.5, 20.0)

# Set {} - Removes duplicates automatically!
unique_ids = {1, 2, 2, 3, 3, 4} 
print(unique_ids) # Output: {1, 2, 3, 4}'''
    },
    {
        "title": "For & While Loops",
        "desc": "Iterate over collections effortlessly or run blocks of code until a specific condition is met.",
        "code": '''# For loop
for x in range(1, 4):  # loops through 1, 2, 3
    print(x)

# While loop
count = 3
while count > 0:
    print(count)
    count -= 1         # Stop condition'''
    },
    {
        "title": "Functions",
        "desc": "Encapsulate logic into reusable blocks and easily define default parameters.",
        "code": '''def greet(name, msg="Welcome!"):
    return f"Hello {name}, {msg}"

print(greet("Vinodh")) 
# Output: Hello Vinodh, Welcome!

print(greet("Nanditha", "Good morning!"))
# Output: Hello Nanditha, Good morning!'''
    },
    {
        "title": "*args & **kwargs",
        "desc": "Want to accept an unlimited number of arguments in a function? Use *args and **kwargs!",
        "code": '''def calculate_total(*args, **kwargs):
    # 'args' is treated as a Tuple of values
    total = sum(args)
    
    # 'kwargs' is treated as a Dictionary
    currency = kwargs.get("currency", "$")
    
    return f"{currency}{total}"

# Handled smoothly!
print(calculate_total(10, 20, 30, currency="€")) # Output: €60'''
    }
]

output_file = "d:/Pythonbase/PythonProjects/LinkedIn_Posts_Complete.md"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("# 🚀 Python Mastery Series - Concise LinkedIn Posts 🐍\n\n")
    f.write("Below are hyper-condensed, highly readable sample code posts for LinkedIn.\n")
    f.write("-----------------------------------------------------------------------\n\n")
    
    for i, post in enumerate(posts, start=1):
        md = f"🚀 **Topic {i}: {post['title']}** 🐍\n\n"
        md += f"Hey network! 👋 {post['desc']}\n\n"
        md += "```python\n"
        md += post['code'] + "\n"
        md += "```\n\n"
        md += "What are your thoughts on this? Drop a comment below! 👇\n\n"
        md += "#Python #Coding #Developer #Programming\n"
        
        f.write(md)
        f.write("\n\n---\n\n")

print("Successfully wrote short and punchy code snippets to LinkedIn_Posts_Complete.md")
