🚀 **Python Mastery Series - Topic 4: Typecasting Input Values!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **Typecasting Input Values** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
# Typecasting input values

# Rectangle area calculation
length = input("Enter the length of the rectangle: ")   
width = input("Enter the width of the rectangle: ")
length = float(length)  # Typecasting input value to float
width = float(width)  # Typecasting input value to float
area = length * width
print(f"The area of the rectangle is: {area} CM²")  

# Excerise 2 : Shopping Cart Application
# 1. Add item to cart
# 2. View cart  
item = input("Enter the item you want to add to the cart: ")
price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))
total = price * quantity
print(f"{quantity} {item}(s) added to the cart. Total price: ${total:.2f}")

# Madlib Game
# A word game where you create a story by filling in the blanks with different words.
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter an adjective: ")
print("Here is your Madlib story:")
print(f"Once upon a time, there was a {adjective1} {noun1} who loved {verb1}.")
print(f"One day, the {noun1} met a {adjective2} friend.")
print(f"They decided to go on an adventure to find a {adjective3} treasure.")
print("The end!")
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming