# python object oriented programming 
# Object - and Classes
class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def __repr__(self):
        return ({self.model},{self.year},{self.color},{self.for_sale})


c1 = Car("Mustang",2004,"red",False)
print(c1.model)