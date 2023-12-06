# classwork3
# open loop, stops when input is 'STOP' or 'stop'
# input = () --> multiple inputs
# 1)name, 2)age, 3)weight, 4)height
# dict={Name: {age: 23, weight: 72, height: 173}}
# 3 minimum data
# with for loop go though dict
# print('Josh is 23 years old and his weight is 72 kg and height is 173 sm')

data = {}

while True:

    name = input('Please insert your name --> ')
    if name == 'stop' or name == 'Stop' or name =='STOP':
        break

    age = input('Please insert your age --> ')
    if age == 'stop' or age == 'Stop' or age =='STOP':
        break

    weight = input('Please insert your weight --> ')
    if weight == 'stop' or weight == 'Stop' or weight =='STOP':
        break

    height = input('Please insert your height --> ')
    if height == 'stop' or height == 'Stop' or height =='STOP':
        break

    data[name] = {'age':age, 'weight':weight, 'height':height}

for name, data in data.items():
    print(f'{name} is {data['age']} years old and their weight is {data['weight']} kg and their height is {data['height']} sm')




