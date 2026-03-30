🚀 **Python Mastery Series - Topic 9: Format Specifiers!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **Format Specifiers** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
# format specifiers
name = "Vinodh"
age = 45    
height = 5.9
is_student = False  
print("Name: %s" % name)  # String
print("Age: %d" % age)    # Integer     

print("Height: %.1f" % height)  # Float with 1 decimal place
print("Height: %.2f" % height)  # Float with 2 decimal places   
print("Height: %.3f" % height)  # Float with 3 decimal places
print("Height: %.4f" % height)  # Float with 4 decimal places   
print("Am I a student? %s" % is_student)  # Boolean 
print("Am I a student? %r" % is_student)  # Boolean (using %r for representation)
print("Hello, %s! You are %d years old." % (name, age))  # Multiple values
print("Hello, %s! You are %d years old and %.1f feet tall." % (name, age, height))  # Multiple values with float
# f-strings (formatted string literals)
print(f"Hello, {name}! You are {age} years old.")
print(f"Hello, {name}! You are {age} years old and {height:.1f} feet tall.")
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming