🚀 **Python Mastery Series - Topic 17: Returning Values From Functions!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **Returning Values From Functions** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
# Returning values from functions
def defadd(a, b):
    return a + b
c = defadd(5, 10)
print(c)  # Output: 15

# Default Arugments - A function that takes default arguments if no arguments are provided during the function call.
# 1. positional  2. keyword  3. default 4. arbitrary

def net_price(price, discount = 0.1, tax=0.05):
    return price * (1-discount)*(1+tax)

price1 = net_price(23)  # Using default discount and tax
print(f"Net price (default discount and tax): ${price1:.2f}")

price2 = net_price(23,0.0,10)  # Using default discount and tax
print(f"Net price (default discount and tax): ${price2:.2f}")

price3 = net_price(23,10)  # Using default discount and tax
print(f"Net price (default discount and tax): ${price3:.2f}")
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming