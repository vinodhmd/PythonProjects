🚀 **Python Mastery Series - Topic 11: While Loop - As Long As A Condition Is True, It Will Execute A Block Of Code Repeatedly!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **While Loop - As Long As A Condition Is True, It Will Execute A Block Of Code Repeatedly** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
# while loop - as long as a condition is true, it will execute a block of code repeatedly
# 
# while condition:
#     # code to be executed  
name = input("Enter your name: ")
while name == "":
    print("Name cannot be empty. Please enter your name.")
    name = input("Enter your name: ")
print(f"Hello, {name}!")

age = input("Enter your age: ")

while not age.isdigit() or int(age) <= 0:
    print("Invalid age entered. Please enter a valid age.")
    age = input("Enter your age: ")

print(f"Nanditha are {age} years old.")

food = input("Enter your favorite food (q to quit): ")
while not food =="q":
    print(f"{food} is a great choice!")
    food = input("Enter your favorite food (q to quit): ")  
print("Goodbye!")

num = int(input("Enter a positive integer (0 to 10): "))
while num <0 or num >10:
    print("Invalid input. Please enter a number between 0 and 10.")
    num = int(input("Enter a positive integer (0 to 10): "))
print(f"You entered: {num}")

# Python compund interest calculator
principal =0;
rate =0;
time =0;
amount =0;
compound_interest =0;
while principal <=0:
    principal = float(input("Enter the principal amount (greater than 0): "))
    if principal <=0:
        print("Principal amount must be greater than 0. Please try again.")

print(f"Principal amount: {principal}")
while rate <=0:
    rate = float(input("Enter the interest rate (greater than 0): "))
    if rate <=0:
        print("Interest rate must be greater than 0. Please try again.")

print(f"Interest rate: {rate}")
while time <=0:
    time = int(input("Enter the time in years (greater than 0): "))
    if time <=0:
        print("Time must be greater than 0. Please try again.")

print(f"Time in years: {time}")

# Calculate compound interest
amount = principal * pow((1 + rate / 100), time)
compound_interest = amount - principal

print(f"Compound interest: {compound_interest}")
print(f"Total amount (principal + interest): {amount}")
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming