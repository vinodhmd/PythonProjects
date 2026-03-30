🚀 **Python Mastery Series - Topic 19: A Function That Takes Arbitrary Number Of Arguments During The Function Call.!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **A Function That Takes Arbitrary Number Of Arguments During The Function Call.** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
# A function that takes arbitrary number of arguments during the function call.
# *args - non-keyword arguments
# **kwargs - keyword arguments
def add_def(*args):
    total = 0
    for num in args:
        total += num
    return total

sum1 = add_def(1, 2, 3)
print(f"Sum (1, 2, 3): {sum1}")  #

def def_displayname(**args):
    for key, value in args.items():
        print(f"{key}: {value}")
        print()
def_displayname(fname="Vinodh", lname="Kumar", title="Mr.")
def_displayname(title="Ms.", lname="Nanditha", fname="S")

def def_address(**kwargs):
    for key in kwargs.keys():
        print(f"{key}")
        print()

def_displayname(street="123 Main St", city="Anytown", state="CA", zip="12345")

def shipping_label(*args, **kwargs):
    print("Shipping Label:")
    for arg in args:
        print(arg,end ="")
    print()
    for value in kwargs.values():
        print(value,end ="")
    print()
    print("---------------------")
    print(f"{kwargs.get('street')  }, {kwargs.get('city')}, {kwargs.get('state')} - {kwargs.get('zip')}")
    print(f"Total items in shipping label: {len(args) + len(kwargs)}")

shipping_label("Hello!","Dr..","Vinodh Kumar", street="6 Gopinathan Gross St.", city="Chennai", state="TamilNadu", zip="600091")
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming