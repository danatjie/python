math ={'Madi':78, 'Josh': 90, 'Bakhytzhan': 100}

def teacher_choose_action():
    teacher_choice = input('Please choose action\n1)check grades\n2)exit\n')
    if teacher_choice == '2':
        print('Exiting')
        return 
    if teacher_choice == '1':
        lesson = input('Please choose the subject\n') 
        name = input('Please enter student name\n')
        if lesson == 'math' and name in math:
            print(f'Grade for {name} in Math: {math[name]}')
        else:
            print(f'Sorry, {name} or the lesson choice is not found')
    

def start():
    while True:
        user = input('Are you a teacher?\n')
        if user == 'yes':
            teacher_choose_action()
        if user == 'no':
            print('if you are not teacher, you cannot access this information')
            break
