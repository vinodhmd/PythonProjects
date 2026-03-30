🚀 **Python Mastery Series - Topic 10: String Methods!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **String Methods** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
# String methods
text = "  Hello, World! Welcome to Python programming.  "   
print(text.lower())  # Convert to lowercase
print(text.upper())  # Convert to uppercase
print(text.strip())  # Remove leading and trailing whitespace
print(text.replace("World", "Universe"))  # Replace substring
print(text.split())  # Split string into a list of words
print(text.find("Python"))  # Find substring index  
print(text.count("o"))  # Count occurrences of a substring
print(text.startswith("  Hello"))  # Check if string starts with a substring
print(text.endswith("programming.  "))  # Check if string ends with a substring
print(len(text))  # Get the length of the string
print(text.index("Python"))  # Get the index of a substring (raises error if not found)
print(text.isalpha())  # Check if all characters are alphabetic 
print(text.isdigit())  # Check if all characters are digits
print(text.isspace())  # Check if all characters are whitespace 
print(text.capitalize())  # Capitalize the first character
print(text.title())  # Capitalize the first character of each word
print(text.center(50))  # Center the string within a specified width
print(text.ljust(50))  # Left-justify the string within a specified width
print(text.rjust(50))  # Right-justify the string within a specified width
print(text.zfill(50))  # Pad the string with zeros on the left to a specified width

# String indexing and slicing
sample = "Hello, World!"
print(sample[0])    # First character   
print(sample[-1])   # Last character
print(sample[0:5])  # Substring from index 0 to 4   
print(sample[7:])   # Substring from index 7 to end
print(sample[:5])   # Substring from start to index 4   
print(sample[::2])  # Every second character
print(sample[::-1]) # Reverse the string    
# List = A collection which is ordered and changeable. Allows duplicate members.
fruits = ["apple", "banana", "cherry"]  
fruits.append("orange")  # Add an item to the end of the list
fruits.insert(1, "kiwi")  # Insert an item at a specific position
print(fruits)  # Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange']
print(fruits[0])  # Output: apple   
print(fruits[-1])  # Output: orange
print(fruits[1:3])  # Output: ['kiwi', 'banana']    
fruits.remove("banana")  # Remove an item by value
fruits.pop()  # Remove the last item
print(fruits)  # Output: ['apple', 'kiwi', 'cherry']
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming