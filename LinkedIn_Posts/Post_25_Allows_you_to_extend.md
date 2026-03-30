🚀 **Python Mastery Series - Topic 25: Allows You To Extend The Functionality Of The Inherited Methods!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **Allows You To Extend The Functionality Of The Inherited Methods** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
# Allows you to extend the functionality of the inherited methods
class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius
    def describe(self):
        print(f"It is a circle wiht {self.color} and Radious of the circle is {3.14 * self.radius * self.radius}cm^2")
        super().describe()
class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width = width
    def describe(self):
        print(f"It is a square with {self.color} and Radious of the circle is {self.width * self.width}cm^2")
        super().describe()
class Triangle(Shape):
    def __init__(self,width,color,is_filled,height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f"It is a Triangle with {self.color} and Radious of the circle is {self.width * self.height}cm^2")
        super().describe()

circle = Circle("Yellow",True,10)
square = Square("Green",False,1)
triangle = Triangle("RED",False,6,6)
print(circle.color, circle.is_filled , circle.radius)
circle.describe()
print(square.color, square.is_filled , square.width)
square.describe()
print(triangle.color, triangle.is_filled , triangle.width, triangle.height)
triangle.describe()

# Polymorphism - Have Many forms or faces
#1.Inheritance - An object could be treated of the same types a parent class
#2."Duck typing" - Object must have necessary attributes/methods
from abc import ABC, abstractmethod 
class Shape:
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius**2

class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side**2   
class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return self.base*self.height
class Pizza(Circle):
    def __init__(self,topping,radius):
        self.topping = topping
        super().__init__(radius)
        #self.radius = radius
    
shapes = [Circle(4),Square(5),Triangle(5,5),Pizza("CheessePizza",15)]
for shape in shapes:
    print(f"{shape.area()}  cm2")

# Duck Typing = Another way to achive polymorphism besides Inheritance
# Object must have the minimum necessary attributes and methods
# If it looks like DUCK and quacks like a duck, it must be a duck

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOFF!!!")
class Cat(Animal):
    def speak(self):
        print("MEOW!!!")
class Car():
    alive = False
    def speak(self):
        print("HAUNK!!!!!")

animals=[Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

# Static Method -A Method that belong to a class rather than any object from that class(instance)
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming