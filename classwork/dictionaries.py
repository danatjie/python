
while True:
    d = {}
    name = input('Please insert your name ')
    if name == 'stop' or name == 'Stop' or name =='STOP':
        break
    age = input('Please insert your age ')
    weight = input('Please insert your weight ')
    height = input('Please insert your height ')

    d = {name: {'age': age, 'weight': weight, 'height': height}}
    
    print(f'{name} is {age} years old and their weight is {weight} kg and their height is {height} sm')

    print(d)

