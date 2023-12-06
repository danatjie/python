import json
import sys

my_data = { 'users' :{
    'dana': {
        'type': 'teacher',
        'password': '122',
        'name': 'Dana',
        'surname': 'Tussupbekova',
        'age': 27,
        'isAdmin': True
    },
    'assel': {
        'type': 'student',
        'password': '123',
        'name': 'Assel',
        'surname': 'Tussupbekova',
        'age': 23,
        'isAdmin': False
    },
    'shynar': {
        'type': 'student',
        'password': '124',
        'name': 'Shynar',
        'surname': 'Sailauova',
        'age': 27,
        'isAdmin': False
    }}
}

with open('assignment#3.json', 'w') as file:
    json.dump(my_data, file, indent=3)

def read_json():
    with open('assignment#3.json', 'r') as file:
        json_data = json.load(file)
    username = input('Please enter your username or type exit\n')
    if username == 'exit':
        exit_function()
    if username in json_data['users']:
        password = input('Please enter your password\n')
        if password in json_data['users'][username]['password']:
            print('you are logged in!') 
        elif password not in json_data:
            print('Wrong password, please try again.')
    else:
        print('The given username does not exist, please sign up.')

def update_json():
    with open('assignment#3.json', 'r') as file:
        json_data = json.load(file) 



def exit_function():
    print('Exiting')
    sys.exit()

    

            


while True:
    system_ask = input('Please\nlogin(1)\nsign up(2)\n')
    if system_ask == '1':
        read_json()
    if system_ask == '2':
        update_json()
