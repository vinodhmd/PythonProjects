🚀 **Python Mastery Series - Topic 14: Dictionary = {Key:Value} Unordered, Changeable And Indexed. No Duplicates!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **Dictionary = {Key:Value} Unordered, Changeable And Indexed. No Duplicates** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
# Dictionary = {key:value} unordered, changeable and indexed. No Duplicates
capital = {
    "USA": "Washington, D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
    "France": "Paris"
}   
print(dir(capital))  # List of all attributes and methods of the dictionary object
# print(help(capital))  # Help on dictionary object
print(capital.get("India"))  # Output: New Delhi
print(capital["India"])  # Output: New Delhi
print(capital.get("Germany"))  # Output: Not Found (default value)
if capital.get("Germany"):
    print("Found")
else:
    print("Not Found")

capital.update({"Germany": "Berlin"})  # Add a new key-value pair
print (capital.get("Germany"))
capital.pop("Russia")  # Remove a key-value pair by key
print(capital)
capital.popitem()  # Remove the last inserted key-value pair
print(capital)
keys = capital.keys()  # Get all keys
values = capital.values()  # Get all values
for key in capital.keys():
    print(key)
    print(values)

# items = capital.items()  # Get all key-value pairs
for key, value in capital.items():
    print(f"The capital of {key} is {value}")   

# Consession stand application
menu = {
    "Hot Dog": 3.50,
    "Popcorn": 2.50,
    "Soda": 1.50,
    "Candy": 1.00
}
cart = []
total = 0
print("Welcome to the Movie Theater Concession Stand!")
print("------------------Menu:")  
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    item = input("Enter the item to add to the cart (or 'q' to quit): ")
    if item.lower() == 'q':
        break
    elif menu.get(item) is not None:
        cart.append(item)
        print("Item are added in the menu. Please try again.")
print()
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming