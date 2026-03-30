🚀 **Python Mastery Series - Topic 7: If Conditional Statements (If, Elif, Else)!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **If Conditional Statements (If, Elif, Else)** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
# if conditional statements (if, elif, else)
# 1. if statement   
age = int(input("Enter your age: "))
if age >= 18 and age < 100:  
    print("You are eligible to vote.")
elif age <= 0:
    print("Invalid age entered.")
elif age >= 100:
    print("You are eligible for a senior citizen discount.")
else:
    print("You are not eligible to vote.")  

response = input("Do you want to continue? (y/n): ").lower()
if response == "y":
    print("You chose to continue.") 
elif response == "n":
    print("You chose not to continue.") 
#--------------------------------- 11 October 2025 ---------------------------------
# Python Calculator Application
print("Welcome to the Python Calculator!")
num1 = float(input("Enter the first number: "))
char = input("Enter an operator (+, -, *, /, %, **, //): ")
num2 = float(input("Enter the second number: "))
print("Result:")
if char == "+":
    print(num1 + num2)
elif char == "-":
    print(num1 - num2)
elif char == "*":
    print(num1 * num2)
elif char == "/":
    print(num1 / num2)
elif char == "%":
    print(num1 % num2)
elif char == "**":
    print(num1 ** num2)
elif char == "//":
    print(num1 // num2)
else:
    print("Invalid operator!")
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming