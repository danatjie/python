import math 

class Person:
    def __init__(self, name, age, energy = 100, weight = 60, happiness = 100):
        self.name = name 
        self.age = age
        self.weight = weight
        self.energy = energy
        self.happiness = happiness
    

    def info(self):
        print(f'Their name is {self.name}')
        print(f'They are {self.age} years old')
        print(f'Their energy is {self.energy}')
        print(f'Their weight is {self.weight}')
        print(f'Their happiness stands at {self.happiness}')

    def sasha_eats(self):
        print('Sasha is having breakfast')
        self.weight += 0.300

    def sasha_in_bathroom(self):
        print('Sasha is going to bathroom')
        self.weight -= 0.400

    def sasha_homework(self):
        print('Sasha is doing homework')
        self.energy -= 15
        if 55<=self.energy<=85:
            print('You should take a rest')
        if 25<=self.energy<=40:
            print('You should sleep')
        if self.energy<=10: 
            print('GET A REST NOW!')
    
    def sasha_rest(self):
        print('Sasha is getting rest')
        self.energy += 20

    def sasha_sleeps(self):
        print('Sasha is sleeping')
        self.energy = 100
    
    def sasha_in_gym(self):
        print('Sasha is working out')
        self.energy-=25
        if self.energy <=10:
            print('It is enough, you should stop')


    def sasha_in_cinema(self):
        print('Sasha enjoyes watching movie')
        self.happiness += 25


       
person = Person('Sasha', 18)

person.info()
person.sasha_eats()
person.sasha_eats()
person.info()
person.sasha_in_bathroom()
person.sasha_in_bathroom()
person.info()
person.sasha_homework() 
person.sasha_homework() 
person.sasha_homework() 
person.info()
person.sasha_rest()
person.sasha_rest()
person.sasha_rest()
person.info()
person.sasha_sleeps()
person.info()
person.sasha_in_gym()
person.sasha_in_gym()
person.sasha_in_gym()
person.sasha_in_gym()
person.info()
person.sasha_sleeps()
person.info()
person.sasha_in_cinema()
person.info()