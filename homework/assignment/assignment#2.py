
data = {
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
        'age': 27,  # Corrected typo here
        'isAdmin': False
    }
}

# infinite loop (system) +
# ask login or signup (register) +
# implement login system with function +
# implement signup with function +
# 1) is it Admin +
#   1.1) Admin can do anything +
#   1.1.1) Can make others as an Admin +
#   1.1.2) Can change type of an account of all users +
#   1.1.3) Can change anything name, surname, age, but can not change password and username +
#   1.1.4) All functions of Teacher and Student 
# 2) if not admin: check type  (Student or Teacher) 
# 3) if Student : student actions
# 4) if Teacher: teacher actions
# logout!!!
# exit() button

import sys

def log_in():
    username = input('Please enter your username or type exit\n')
    if username == 'exit':
        exit_function()
    if username in data:
        password = input('Please enter your password\n')
        if password in data[username]['password']:
            print('you are logged in!')
            ask_admin = input('Are you admin?\nyes\nno\n')
            if ask_admin == 'yes':
                if username in data and data[username]['isAdmin']:
                    print('Admin access granted')
                    admin_actions()
            if ask_admin == 'no':
                check_type = input('Are you teacher or student?\n')
                if check_type == 'teacher':
                    teacher_actions()
                if check_type == 'student':
                    student_actions()    
        elif password not in data:
            print('Wrong password, please try again.')
    else:
        print('The given username does not exist, please sign up.')
    
def sign_up():
    new_username = input('Please create username or type exit\n')
    if new_username == 'exit':
        exit_function()
    new_password = input('Please create unique password\n')
    data[new_username] = {'password': new_password}

def admin_actions():
    choice_action = input('Please choose the action-->\nmake this user admin(1)\nchange data for this user(2)\n')
    if choice_action == '1':
        choose_user = input('Please choose the user\n')
        if choose_user in data:
            make_admin = input('Are you sure you want this user to be Admin?\n')
            if make_admin == 'yes':
                data[choose_user]['isAdmin'] = True
            else:
                data[choose_user]['isAdmin'] = False
    if choice_action == '2':
        choose_user = input('Please choose the user\n')
        if choose_user in data:
            change_data = input('What do you want to change?\n')
            if change_data == 'password' or change_data == 'username':
                print('You are not allowed to change this data')
            elif change_data in data[choose_user]:
                new_data = input('Please insert new data --> ')
                data[choose_user][change_data] = new_data
      
def teacher_actions():
    teacher_action = input('Would you like to see students data?\n')
    if teacher_action == 'yes':
        choose_student = input('Please choose student or all\n')
        if choose_student == 'all':
            for student_name, student_data in data.items():
                if student_data['type'] == 'student':
                    print(student_data)
        else:
            student_data = data.get(choose_student)
            if student_data and student_data['type'] == 'student':
                print(student_data)
            else:
                print('Invalid input or student not found.')

def student_actions():
    student_action = input('Would you like to see your data?\n')
    if student_action == 'yes':
        name = input('Please enter your username\n')
        if name in data:
            print(data[name])
        else:
            print('Invalid input or student not found.')

def exit_function():
    print('Exiting')
    sys.exit()

while True:
    system_ask = input('Please\nlogin(1)\nsign up(2)\n')
    if system_ask == '1':
        log_in()
    if system_ask == '2':
        sign_up()
