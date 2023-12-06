from abc import abstractclassmethod

class Car:
    def __init__(self, name, color, type):
        self.__name = name
        self.__color = color
        self.__type = type

    def get_name(self):
        print(self.__name)
        
    def get_color(self): 
        print(self.__color)

    def get_type(self):   
        print(self.__type)
        
    def set_name(self, name): #we changed name here #need to write 2 positional arguments self and what you change
        self.__name = name
    
    @staticmethod
    def print_greetings(value):
        print('Hi ' + value + '!')

    @abstractclassmethod
    def print_goodbyes(self, value):
        print('Bye ' + value + '!')

car = Car('Kia', 'green', 'mechanical')
car.set_name('Corolla')

car.get_name()
car.get_color()
car.get_type()

Car.print_greetings('customer')
Car.print_goodbyes('customer')



class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__type = type

class Animal(Lion):
    def __init__(self, name, age):
    super.__init__(name, age)
