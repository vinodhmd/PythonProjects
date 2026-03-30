🚀 **Python Mastery Series - Topic 26: Usually Used For General Utility Functions.!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **Usually Used For General Utility Functions.** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
# Usually used for general utility functions.

# Instance method - best for operations on iteration of the class(objects)
# Static method -  best utility functions that do not need access to class data
class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position
    def get_info(self):
        return f"{self.name} = {self.position}"
    @staticmethod
    def is_vaild_position(position):
        vaild_position = ["Manager", "Software","Cook"]
        return position in vaild_position

print(Employee.is_vaild_position("Manager"))
employee1 = Employee("Vinodh", "Software")
employee2 = Employee("Raja", "Manager")
employee3 = Employee("Nani", "Cook")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

#Class Method - Allow operations related to the class itself
                #Take (cls) as the first parameter , which reprents the class itself
                # 
# Instance Method - Best for operation on instance of the class(objects)
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming