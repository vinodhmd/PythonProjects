🚀 **Python Mastery Series - Topic 28: Threading.Thread(Target=My_Function)!** 🐍

Hey network! 👋 Today I'm sharing some sample code on **Threading.Thread(Target=My_Function)** in Python. Whether you're a beginner or just brushing up your basics, I hope you find this useful! 👇

```python
# Threading.Thread(Target=my_function)
def walk_dog(first):
    time.sleep(8)
    print(f"You Finished walking the {first } Dog!!!")

def take_out_trash():
    time.sleep(2)
    print(f"You Finished out the Trash cleaup!!!")

def get_mail():
    time.sleep(2)
    print(f"You Got the Mail!!!")

#walk_dog()
#take_out_trash()
#get_mail()

chore1 = threading.Thread(target=walk_dog("Scooby"))
chore1.start()
chore2 = threading.Thread(target=take_out_trash)
chore2.start()
chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()
print("All chore Jbs are completed")

# Connect PokeAPI using Python

base_url = "https://pokeapi.co/api/v2/"

def get_pokeman_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response)
    if response.status_code ==200:
        print("Processed the Request APIs!!!")
        pokeman_name = response.json()
        return pokeman_name
    else:
        print("Not Processed the Request APIs!!!")

pokeman_name = "pikachu"
pokeman_info = get_pokeman_info(pokeman_name)
if pokeman_info:
    pass
    #print(f"{pokeman_info["name"]}")
    #print(f"{pokeman_info["order"]}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Om Siva")
        self.setGeometry(700,150,500,500)
        self.setWindowIcon(QIcon("OmSivaImage.jpeg"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()


# End of the program
print("Thank you for using the Python program. Goodbye!")

#Sum the numbers in the list
numbers = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for number in numbers:
    sum += number
print(sum)
```

What are your favorite tips regarding this topic? Let me know in the comments! 💬

#Python #Coding #Programming #Developer #Learning #Tech #PythonProgramming