🚀 **Python Mastery Series - Topic 15: Random Numbers!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **Random Numbers** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
# Random Numbers

low =1;
high =100;

number = random.randint(low, high) 
print(number)
options = ("Rock","Scissors","Paper")
option = random.choice(options)
print(option)

cards = ["2","3","4","5","6","7","8","9","10","A","J","Q","K"]
random.shuffle(cards)
print(cards)

# Python Number Guessing Game
low_num =1;
high_num =10;
answer = random.randint(low_num , high_num)
print(answer)

guesses =0
is_running = True
print("---------------------Python Number Guessing Game---")
print(f"Select a Number between {low_num} and {high_num}")

while is_running:
    guess  = input("Enter your Guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess <low_num or guess>high_num:
            print("Sorry...Out of Range")
            print(f"Please select a Number between {low_num} and {high_num}")
        elif guess < answer:
            print("Too Low! Guess Again!")
        elif guess > answer:
            print("Too High! Guess Again!")
        else:
            print(f"You are Correct! The Answer is {answer}")
            print(f"Total No of Guess {guesses}")
            is_running = False
    else:
        print("Sorry....Guess accept by Numbers only!")
        print(f"Please select a Number between {low_num} and {high_num}")

# ⭐ rock, paper, scissors game 🗿

options = ("rock","paper","scissors")
running = True
while running:
    player = None
    computer = random.choice(options)
    while player is not options:
        player = input("Enter a choice like rock, paper, scissors game ")
        print(f"player Choice Is: {player}")
        print(f"Computer Choice Is:{computer}")

    if player == computer:
        print("Its Tie!")
    elif player =="rock" and computer == "scissors":
        print("You Win!")
    elif player =="paper" and computer == "rock":
        print("You Win!")
    elif player =="scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You loser!")
    if not input("Play Again ?? ()y/n").lower =="y":
        running = False

print("Thanks for Playing!")
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming