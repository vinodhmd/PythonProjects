🚀 **Python Mastery Series - Topic 13: Collections - List, Tuple, Set, Dictionary!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **Collections - List, Tuple, Set, Dictionary** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
# Collections - List, Tuple, Set, Dictionary
# List = [] ordered and changeable. Duplicates OK
# Set ={} unordered and immutable, but add/remove OK. No Duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER
# Dictionary = {key:value} unordered, changeable and indexed. No Duplicates

#List
fruits = ["apple", "banana", "cherry","coconut","orange"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
print(fruits[0])  # Output: apple   
print(fruits[-1])  # Output: orange
print(fruits[1:3])  # Output: ['banana', 'cherry']
print(fruits[::2])  # Output: ['apple', 'cherry', 'orange']
print(fruits[::-1]) # Output: ['orange', 'coconut', 'cherry', 'banana', 'apple']
fruits[0] = "kiwi"  # Change the value of the first item
print(fruits)  # Output: ['kiwi', 'banana', 'cherry']   
for fruit in fruits:
    print(fruit)
#print(dir(fruits))  # List of all attributes and methods of the list object
#print(help(fruits))
print(len(fruits))  # Output: 5
print(max(fruits))  # Output: orange (based on alphabetical order)
print(min(fruits))  # Output: banana (based on alphabetical order)  
print("banana" in fruits)  # Output: True
fruits.append("mango")  # Add an item to the end of the list
fruits.insert(1, "grape")  # Insert an item at a specific position
print(fruits)  # Output: ['kiwi', 'grape', 'banana', 'cherry', 'coconut', 'orange', 'mango']
fruits.remove("banana")  # Remove an item by value  
fruits.pop()  # Remove the last item
print(fruits)  # Output: ['kiwi', 'grape', 'cherry', 'coconut', 'orange']
fruits.sort()  # Sort the list in ascending order  
print(fruits)  # Output: ['cherry', 'coconut', 'grape', 'kiwi', 'orange']
fruits.sort(reverse=True)  # Sort the list in descending order
print(fruits)  # Output: ['orange', 'kiwi', 'grape', 'coconut', 'cherry']
#fruits.clear()  # Remove all items from the list
print(fruits)  # Output: []

# Set ={} unordered and immutable, but add/remove OK. No Duplicates
fruits = {"apple", "banana", "cherry","coconut","orange"}
print(fruits)
print("banana" in fruits)  # Output: True
fruits.add("mango")  # Add an item to the set
fruits.remove("banana")  # Remove an item by value  
fruits.discard("grape")  # Remove an item by value (no error if not found)
print(len(fruits))  # Output: 4
print(fruits)

# Tuple = () ordered and unchangeable. Duplicates OK. FASTER
fruits = ("apple", "banana", "cherry","coconut","orange")   

print(len(fruits))
# print(help(fruits))
print(fruits.index("cherry"))  # Output: 2
print(fruits.count("cherry"))  # Output: 2
for fruit in fruits:
    print(fruit)
#print(fruits)

# Shopping Cart Application
foods = []
prices=[]
total=0
while True:
    food = input("Enter the item to add to the cart (or 'q' to quit): ")
    if food.lower() == 'q':
        break   
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("------------------------------YOUR CART------------------------------")
for food in foods:
    print(f"- {food}", end="")

for price in prices:
    print()
    
    print(f"- {price}", end="")


print(f"\nTotal price: ${total:.2f}")
total += price
 
# two dimensional list (list inside a list)

fruits = ("apple", "banana", "cherry","coconut","orange")
vegetables = ("carrot", "broccoli", "spinach","potato","onion")
meats = ("chicken", "beef", "pork","fish","lamb")
drinks = ("water", "soda", "juice","coffee","tea")  
groceries = [fruits, vegetables, meats, drinks]
print(groceries)
print(groceries[0])  # Output: ('apple', 'banana', 'cherry', 'coconut', 'orange')
print(groceries[1])  # Output: ('carrot', 'broccoli',   'spinach', 'potato', 'onion')
print(groceries[2])  # Output: ('chicken', 'beef', 'pork', 'fish', 'lamb')
print(groceries[3])  # Output: ('water', 'soda', 'juice', 'coffee', 'tea')
print(groceries[0][0])  # Output: apple
print(groceries[1][1])  # Output: broccoli      

for collection in groceries:
    print(collection)
    for item in collection:
        print(item)
   
# Print Phone Keypad
keypad = (
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "#"]
)
for row in keypad:
    for key in row:
        print(key, end=" ")
    print()  # New line after each row

# Python Quiz Application
questions = ("What is the capital of France?",
             "What is 2 + 2?",  
             "What is the largest planet in our solar system?",
             "Who wrote 'To Kill a Mockingbird'?",
             "What is the chemical symbol for water?",)
options = ((),
        ("A. Paris", "B. London", "C. Berlin", "D. Madrid"),
        ("A. 3", "B. 4", "C. 5", "D. 6"),
        ("A. Jupiter", "B. Mars", "C. Earth", "D. Saturn"),
        ("A. Harper Lee", "B. Mark Twain", "C. Ernest Hemingway", "D. F. Scott Fitzgerald"),
        ("A. H2O", "B. O2", "C. CO2", "D. N2") )
answers = ("A. Paris", "B. 4", "C. Jupiter", "D. Harper Lee", "E. H2O")
guesses = []
score = 0
question_num = 0

for question in questions:
    print ("------------------------------ QUESTION------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D or E): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is: {answers[question_num]}")
    question_num += 1    

print("------------------------------ RESULTS ------------------------------")
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")      
print()
print("Guesses: ", end="")  
for guess in guesses:
    print(guess, end=" ")
print()
score_percentage = int((score / len(questions)) * 100)  
print(f"Your score is: {score}/{len(questions)} ({score_percentage}%)")
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming