🚀 **Python Mastery Series - Topic 24: E - Enclosing (Scope Of Enclosing Functions)!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **E - Enclosing (Scope Of Enclosing Functions)** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
# E - Enclosing (scope of enclosing functions)   
def fun3():
    #x=4
    def fun4():
        x=4
        print(x)
    fun4()
    #print(x)

fun3()  
# G - Global (module level scope)
x=10000
def fun5():
    #x=1
    print(x)

def fun6():
    #x=2
    print(x+1)

fun5()
fun6()
# B - Built-in (scope of built-in names)
import math as e
def fun7():
    #x=2
    print(e.sqrt(16))
fun7()

# if __name__ == "__main__": (this block will run only if the module is run directly, not when imported )
def main():
    print("This is the main function.")
    # You can add more code here that you want to run when the module is executed directly.

if __name__ == "__main__":
    main()

# Python Banking Application
def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")

def deposit(balance):
    amount = float(input("Enter the amount to deposit: $"))
    if amount <= 0:
        print("Deposit amount must be positive.")
        return 0
    return amount

def withdraw():
    amount = float(input("Enter the amount to withdraw: $"))
    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return 0
    elif amount > balance:
        print("Insufficient funds.")
        return 0
    else:
        return amount

balance = 0.0
is_running = True
while is_running:
    print("\n--- Python Banking Application ---")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    match choice:
        case "1":
            show_balance(balance)
        case "2":
            balance += deposit()
        case "3":
            balance -= withdraw()
        case "4":
            print("Thank you for using the Python Banking Application. Goodbye!")
            is_running = False
        case _:
            print("Invalid choice. Please try again.")

# Python slot machines

def spin_slots():
    symbols = ["🍒","🍋","🍉","🔔","⭐"]
    results =[random.choice(symbols) for _ in range(3)]
    #for symbol in range(1):
    #    results.append(random.choice(symbols))
    #return results

def print_slots(row):
    print("|',{row}")

def getpayout(row, bet):
    if row[0]==row[1]==row==[2]:
        if row[0]=="🍒":
            return bet * 3
        elif row[0]=="🍋":
            return bet * 4
        elif row[0]=="🍉":
            return bet * 5
        elif row[0]=="🔔":
            return bet * 6  
        elif row[0]=="⭐":
            return bet * 7
    return 0   


def main():
    balance = 100
    print(f"Your starting balance is: ${balance:.2f}")
    print("Spinning the slots...")
    print("🍒🍋🍉🔔⭐")
    while balance > 0:
        print(f"Your starting balance is: ${balance:.2f}")
        bet = input("Enter your bet amount: $")
        if not bet.isdigit():
            print("Bet amount must be positive.")
            continue
        bet = int(bet )
        if bet <= 0:
            print("Bet amount must be positive.")
            continue
        elif bet > balance:
            print("Insufficient funds.")
            continue
        balance -= bet
        row = spin_slots()
        print("Spinning.....\n") 
        print_slots(row)
    #spin_slots()
    #print_slots()
    payout = getpayout(row,bet)
    if(payout>0):
        print("You Won the Amt ${payout}")
        balance +=payout    
    else:
        print("Better luck next time")

if __name__ == "__main__":
    main()


# Encryption program
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
#print(f"chars:{chars}")
#print(f"key:{key}")

#Encrypt 
plain_text = input("Enter the Message to encrypt:-")
cipher_text =""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"Orginal Message Like : {plain_text}")
print(f"Encrypt Message Like : {cipher_text}")

#Decrypt 
cipher_text = input("Enter the Message to decrypt:-")
plain_text =""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print(f"decrypt Message Like : {cipher_text}")
print(f"Orginal Message Like : {plain_text}")

# Hangman in Python
from wordlist import words
#words = ("apple","orange","banana","cocount","pineapple")
# dictonary key = ()
hangman_art = {0:(
        " ",
        " ",
        " "),
    1:(" o "
       "   "
       "   "),
    2:(" o  "
       " |  "
       "   "),
    3:(" o  "
       "/|  "
       "   "),
    4:(" o  "
       "/|\  "
       "   "),
    5:(" o  "
       "/|\  "
       "/   "),
    6:(" o  "
       "/|\  "
       "/-\  ")}

#print(hangman_art[6])

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        display_answer(answer)
        guess = input("Enter a Letter:").lower()
        if len(guess)!= 1 or not guess.isalpha():
            print("invalid Inputs")
            continue
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        guessed_letters.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i] = guess
        else:
            wrong_guesses +=1
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print(" You Won!!!")
            is_running = False
        elif wrong_guesses >= (len(hangman_art) -1):
            display_man(wrong_guesses)
            display_answer(answer)
            print(" You Loosser !!!")
            is_running = False    
if __name__ == "__main__":
    main()

# python object oriented programming 
# Object - and Classes
class Car:
        def __init__(self, model, color, year): # Correct __init__ with arguments
            self.model = model
            self.color = color
            self.year = year
        def drive(self):
            print(f"You Can drive the {self.model}")
        def stop(self):
            print(f"You Can stop the  {self.model}")
        def describe(self):
            print(f"You are driving {self.year} and {self.model} and color is {self.color}")

# Now you can create a Car object with arguments
my_car = Car("Tesla Model 3", "Red", 2023)
print(my_car.year)
print(my_car.drive())
print(my_car.stop())
print(my_car.describe())

# Class Variables - shared among all instance of the class
# Define out side of the constructor
# Allow you to share data among all objects created from that classes
class Student:
    class_variables_year =2025
    class_variables_no_student = 15

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.class_variables_no_student +=1

student1 = Student("Vinodh",45)
student2 = Student("Sona",45)

print(student1.name)
print(student2.name)
print(Student.class_variables_year)
print(Student.class_variables_no_student)

# Inheritance = Allows a class to inherit attributes from another clasess
# helps with code resuablity and extensiblity
# class child(Parent)
# Eg:- Animal - > Dog ->Cat -> Mouse
class Animals:
    speaks = ""
    def __init__(self,name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is Eating")
    def sleep(self):
        print(f"{self.name} is Sleeping")
    
class Dog(Animals):
    def speak(self):
        print("!!!SAPARK!!!")

class Cat(Animals):
    def speak(self):
        print("!!!MEOW!!!")

class Mouse(Animals):
    def speak(self):
        print("!!!SQUEEK!!!")

dog = Dog("Scooby")
cat = Cat("Rose")
mouse = Mouse("roosser")

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
mouse.speak()

# Multiple Inheritance - inherit from more than one parent class c(a,b)
# Multiple level Inheritance -inherit from a parent which inherits from another parent c(B)<->B(A)<>A
class Animal:
    def __init__(self,name):
        self.name = name
        print("Hello")
    def eating(self):
        print(f"{self.name} is eating")
    def sleeping(self):
        print(f" {self.name}  is Sleeping")
class Prey(Animal):
    def flee(self):
        print(f" {self.name}  is fleeing")
class Predator(Animal):
    def hunt(self):
        print(f" {self.name} is hunting")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")
rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
rabbit.sleeping()

# Super () = Funtions used in a child class to call methods from a parent class (super class)
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming