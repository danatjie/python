#practicing functions

def greet():

    print('Hi there')
    print('Welcome aboard')

greet() #here we call function, without calling it it will not print

def greet(first_name, last_name): #parameters in parenthesis

    print(f'Hi {first_name} {last_name}')
    print('Welcome aboard')

greet('Dana', 'Tussupbekova') #arguments
greet('Richard', 'Van Amerom')