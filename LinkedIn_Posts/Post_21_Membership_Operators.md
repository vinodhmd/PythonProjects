🚀 **Python Mastery Series - Topic 21: Membership Operators!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **Membership Operators** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
#Membership Operators
# The 'in' keyword is used to check if a value exists in a sequence (list, tuple, string).
# The 'not in' keyword is used to check if a value does not exist in a sequence.    
word = "Python"
uinput = input("Enter a letter to check if it is in the word 'Python': ")
if uinput in word:
    print(f"'{uinput}' is in the word 'Python'")
else:
    print(f"'{uinput}' is not in the word 'Python'")

students = ["Alice", "Bob", "Charlie"]
student = input("Enter a student name to check if they are in the class: ")
if student not in students:
    print(f"{student} is not in the class.")
else:
    print(f"{student} is in the class.")    

email = "vinodh@example.com"
if "@" in email and "." in email:
    print("Valid email address.")   
else:
    print("Invalid email address.")

# List Comprehensions   - A concise way to create lists using a single line of code.
# Expression  for item in iterable if condition
squares = [x**2 for x in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
dobules = []
for i in range(1, 11):
    dobules.append(i * 2)
print(dobules)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  
grade = [85, 92, 78, 90, 88]
pass_grade = [g for g in grade if g >= 90]
print(pass_grade)  # Output: [85, 92, 90, 88]

# Match Case Statements - A control flow statement that allows you to match a value against multiple cases and execute the corresponding block of code.
# match variable:

def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"

day = int(input("Enter a day number (1-7): "))
print(f"The day is: {day_of_week(day)}")

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "Invalid day"

day = input("Enter a day name (its Weekend ?): ")
print(f"The day is: {is_weekend(day)}")
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming