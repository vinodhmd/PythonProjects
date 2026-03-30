🚀 **Python Mastery Series - Topic 12: For Loops - Used To Iterate Over A Sequence (Like A List, Tuple, Dictionary, Set, Or String)!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **For Loops - Used To Iterate Over A Sequence (Like A List, Tuple, Dictionary, Set, Or String)** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
# For Loops - used to iterate over a sequence (like a list, tuple, dictionary, set, or string)
# for item in sequence: 
# you can iterate over a list, string, tuple, dictionary, set, range() and sequence of numbers

for x in reversed(range(1, 6)):  # Numbers from 1 to 5
    print(x)
print("Finished counting to 5!")

for x in range(1, 10, 2):  # Numbers from 1 to 9, step 2
    print(x)
print("Finished counting to 9!")

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    if x == "-":
        continue  # Skip the hyphen
    print(x)

# Time module
print("Current time in seconds since epoch:", time.time())
local_time = time.localtime()
print("Local time:", local_time)

mytime = int(input("Enter time in seconds to countdown: "))
while mytime > 0:
    mins, secs = divmod(mytime, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    mytime -= 1

for x in range(0,mytime):
    time.sleep(1)
    print(x)

for x1 in range(mytime,0,-1):
    seconds = x1 % 60
    minutes = int ((x1/60)%60)
    hours = int((x1/3600)%24)
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1)
   
print("Time's up!")

# Nested loops - A loop inside another loop
for x in range(3):
    for y in range(1,10):
        print(y,end=' ')
    print()  # New line after inner loop

rows = int(input("Enter number of rows: ") )
colums = int(input("Enter number of colums: ") )
symbol = input("Enter a symbol to use: ")
for x in range(rows):
    for y in range(colums):
        print(symbol,end=' ')
    print()  # New line after inner loop
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming