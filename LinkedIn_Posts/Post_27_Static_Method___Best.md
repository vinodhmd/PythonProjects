🚀 **Python Mastery Series - Topic 27: Static Method - Best For Utility Functions That Do Not Need Access To Class Data!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **Static Method - Best For Utility Functions That Do Not Need Access To Class Data** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
# Static Method - Best for utility functions that do not need access to class data
# Class Method - Best for class_level data or require to the class itself

class Student:
    count = 0
    total_gpa = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
# Instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total No of Students:{cls.count}"

    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA : - {cls.total_gpa/cls.count:.2f}"

Student("spongebob","2.8")
Student("Vinodh","3")
Student("Charu","4.5")
Student("nandthiya","4.8")

print(Student.get_count())
print(Student.get_avg_gpa())

# Magic Method - Dunder methods (double underscore) __init__,__str__,__eq__
# They are automatically called by many of the python built in operations
# They allow developers to define or customize  the behavior of objects

class Book:
    def __init__(self,title,autor,no_pages):
        self.title = title
        self.autor = autor
        self.no_pages = no_pages

    def __str__(self):
        return f"'{self.title}' by {self.autor}"

    def __it__(self,other):
        return self.no_pages == other.no_pages

    def __eq__(self,other):
        return self.title == other.title and self.autor == other.autor

    def __gt__(self,other):
        return self.no_pages >= other.no_pages

    def __add__(self,other):
        return self.no_pages + other.no_pages

    def __contains__(self, keywords):
        return keywords in self.title or keywords in self.autor

    def __additem__(self,key):
        if key == "title":
            return self.title
        if key == "autor":
            return self.autor

    
b1= Book("AAA","Mr.Roo",422)
b2= Book("BBB","Mr.Roo",422)
b3= Book("CCC","Mr.Roo",422)

print(b1)
print(b1 == b2)
print(b2 > b3)
print(b2 + b3)
print("s" in b3)
print(b3['autor'])
print(b3['title'])

# @Property - Decorator used to define a method as a property (it can be accessed like an attribute) 
# Benefit : - add addtional logic when read , write, delete attributes
# Gives you getter ,setter and deleter method
# 
class Rectangle:
    def __init__(self, width,height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f} cms"

    @property
    def height(self):
        return f"{self._height:.1f} cms"

    @width.setter
    def width(self,new_width):
        if new_width >0:
            self._width = new_width
        else:
            print("Width must be greater then zero")

    @height.setter
    def height(self,new_height):
        if new_height >0:
            self._height = new_height
        else:
            print("Height must be greater then zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width info are deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height info are deleted")

rec = Rectangle(3,4)
rec.width = 999
rec.height = 1000

#print(rec.width)
#print(rec.height)

del rec.width
del rec.height

# @ Decorders 
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("Add your MOJ")
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("**************************")
        func(*args, **kwargs)
    return wrapper
@add_fudge  
@add_sprinkles
def get_ice_cream(flavor):
    print("Here is your {flavor} Ice Cream")

get_ice_cream("VANILLA")

# Exceptions - An  event that interrupts the flow of a program
#(ZeroDivisionError,TypeError,ValueError)
# Try,Catch and finally     


try:
    # Try some Code
    number = int(input("Enter Your No:- "))
    print(1/number)
except ZeroDivisionError:
    # Handle Expection
    print("You Cann't divide by Zero")
except ValueError:
    # Handle Expection
    print("You Can enter number only!!!")
except Exception:
    # Handle Expection
    print("Error is here")
finally:
    print("Post work to be handle!!!")

try:
    # Try some Code
except ZeroDivisionError:
    # Handle Expection
except ValueError:
    # Handle Expection
except Exception:
    # Handle Expection
finally:

# Python File detection
file_path = "D:\\Pythonbase\\PythonProjects\\test.txt"
file_dir = "D:\\Pythonbase\\PythonProjects"
if os.path.exists(file_path):
    print("Allowed")
    if os.path.isfile(file_path):
        print("Yaaaaaaa")
    else:
        print("Nooooooo")
elif os.path.isdir(file_dir):
    print("Ya..Floder")
else:
    print("Not Allowed")

# Python writing files like .txt,.json,.csv
employee = ["Vinodh","Charuhetuki","Nanditha","Kalaimathi"]
employee1 = {
    "name": "Vinodh",
    "age":"45",
    "job":"Software Mobile Developer"
}
empcsv = [["Name", "Age", "Job"],
           ["Vinodh","45","UnEmpolyment"],
           ["Charuhetuki","12","Student"],
           ["Nanditha","7","Student"]]
txt_data = "Writing thee files using python functions"
file_dir = "D:\\Pythonbase\\PythonProjects\\"
txtfilepath = file_dir +"output.txt"
jsonfilepath = file_dir +"output.json"
csvfilepath = file_dir +"output.csv"

#with open(file= txtfilepath, mode = "w") as file:
#    file.write(txt_data)
#    print("Done")

try:
    with open(file= txtfilepath, mode = "a") as file:
        for emp in employee:
            file.write("\n"+ emp)
        print("Done")
except FileExistsError:
    print("File Already Avilables!!!")

try:
    with open(file= jsonfilepath, mode = "a") as file:
        json.dump(employee1,file)
        print("Done")
except FileExistsError:
    print("File Already Avilables!!!")

try:
    with open(file= csvfilepath, mode = "a", newline ="") as file:
        writer = csv.writer(file)
        for row in empcsv:
            writer.writerow(row)
        print("Done")
except FileExistsError:
    print("File Already Avilables!!!")

file_dir = "D:\\Pythonbase\\PythonProjects\\"
txtfilepath = file_dir +"output.txt"
jsonfilepath = file_dir +"output.json"
csvfilepath = file_dir +"output.csv"

with open(txtfilepath,"r")as file:
    content = file.read()
    print(content)

with open(jsonfilepath,"r")as file:
    content = json.load(file)
    #for linejson in content:
    print(content)

with open(jsonfilepath,"r")as file:
    content = csv.reader(file)
    for csvline in content:
        print(csvline)

date = datetime.date(2025,1,11)
print(date)

today = datetime.date.today()
print(today)
time1 = datetime.time(12,30,0)
print(time1)
now1 = datetime.datetime.now()
print(now1)
now2 = now1.strftime("%H:%M:%S %d-%m-%y")
print(now2)

targettime = datetime.datetime(2030,1,2,12,30,1)
curgettime = datetime.datetime.now()
if targettime < curgettime :
    print("Target data has passed!!!")
else:
    print("Target data not passed!!!")


def set_alarm_time(alarm_time):
    print(f"Alaram set for {alarm_time}")
    sound_file = "Kandra_Music.mpeg"
    is_running = True

    while is_running:
        currttimenow = datetime.datetime.now().strftime("%H:%M:%S")
        print(currttimenow)
        if currttimenow ==alarm_time:
            print("Wake UP!!!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while  pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False
        time.sleep(1)

if __name__=="__main__":
    alarm_time = input("Enter the Time(HH:MM:SS):")
    set_alarm_time(alarm_time)
    print("Done!!!")

# Multithreading = used to perform multiple taks concurrently (Multitasking)
# Good for I/OBound tasks like reading files or fetching data from APIs
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming