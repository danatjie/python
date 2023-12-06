# We have a program that shows us the score of the student by request
# 1) check if a user is a student or teacher
# 2) Teacher: 
   # 2.1) Which lesson : two choices : 1) Math or 2) English or 3) Exit() (input 1 or 2 or 3)
    # 2.2) Teacher action choice: 1) Check all grades or 2) Change exam points or 3) Exit()
    # 2.3) Function check all grades: print all student grades in this format:
            # Math lesson :
            # Madi : 78 ==> 65
            # Josh : 90 ...         
    # 2.4) Function change exam points : Math students : ['Madi', 'Josh'...]
                                        # Which Students? => take Input(), Madi
                                        # f'{name} current points {math[Madi]}
                                        # For what grade you want you change? => input () 65
                                        # math['Madi'] = 65
# 3) Student: 
    #3.1) Which lesson : two choices : 1) Math or 2) English or 3) Exit() (input 1 or 2 or 3)
    # 3.2) Student action choice: 1) Check grade or 3) Exit()
    # 3.3) Check Grades function: input() a Name
    # 3.4) Print f'{name} has a grade {Math[Name]} in Math
#сделать рейтинг кто pass and fail

math ={'Madi':78, 'Josh': 90, 'Bakhytzhan': 100}
english = {'Madi':65, 'Josh': 100, 'Bakhytzhan': 80}
    
def teacher_choose_action():
    teacher_choice = input('Please choose action 1)check grades 2)change grades 3)see rating 4)exit --> ')
    if teacher_choice == '4':
        exit_function()
        return 
    if teacher_choice == '1':
        teacher_check_grades()
    if teacher_choice == '2':
        teacher_change_grades()
    if teacher_choice == '3':
        pass_and_fail_rating()
  

def teacher_check_grades():
        lesson = input('Please choose 1)Math 2) English or 3)Exit --> ') 
        if lesson == '3':
            exit_function()
            return
        name = input('Please enter student name or choose all --> ')
        if lesson == '1' and name in math:
            print(f'Grade for {name} in Math: {math[name]}')
        elif lesson == '2' and name in english:
            print(f'Grade for {name} in English: {english[name]}')
        elif lesson == '1' and name == 'all':
            print(math)
        elif lesson == '2' and name == 'all':
            print(english)
        else:
            print(f'Sorry, {name} or the lesson choice is not found')
        

def teacher_change_grades():
    change_action = input('Do you want to change grade 1)yes 2)no 3) exit --> ')
    if change_action == '1':
        lesson = input('Please choose 1)Math 2) English or 3)Exit --> ') 
        name = input('Please enter student name--> ')
        new_grade = input ('Please enter new grade --> ')
        if lesson == '1' and name in math:
            print(f'Grade for {name} in Math was changed from {math[name]} to {new_grade}')
            #print(math) does not update the dict
        elif lesson == '2' and name in english:
            print(f'Grade for {name} in English was changed from {english[name]} to {new_grade}')
        else: 
            print(f'Sorry, {name} is not found')
    if change_action =='2':
        teacher_choose_action()
    if change_action == '3':
        exit_function()
        return       

def student_check_grades():
    lesson = input('Please choose 1)Math 2) English or 3)Exit --> ')
    if lesson == '3':
        exit_function()
        return
    name = input('Please enter your name --> ')
    if lesson == '1' and name in math:
        print(f'Grade for {name} in Math: {math[name]}')
    elif lesson == '2' and name in english:
        print(f'Grade for {name} in English: {english[name]}')
    else:
        print(f'Sorry, {name} or the lesson choice is not found')
    
def exit_function():
    print('Exiting')

def pass_and_fail_rating():
    rating = input('Would you like to see student rating? 1) yes 2)no or 3)exit? --> ')
    if rating == '3':
        exit_function()
        return
    if rating == '2':
        teacher_choose_action()
    lesson = input('Please choose the lesson 1)Math 2)English --> ')
    if rating == '1' and lesson =='1':
            for name, grade in math.items():
                if grade > 75:
                    print(f'{name} passed')
                else:
                    print(f'{name} failed')
    if rating == '1' and lesson == '2':
            for name, grade in english.items():
                if grade > 75:
                    print(f'{name} passed')
                else:
                    print(f'{name} failed')
     
while True:
    user = input('Are you a 1)teacher or a 2)student? -->')
    if user == '1':
        teacher_choose_action()
    elif user == '1':
        teacher_check_grades()
    elif user == '1':
        teacher_change_grades()
    elif user == '1':
        pass_and_fail_rating()
    elif user == '2':
        student_check_grades()
    else:
        print('Invalid! Try 1 or 2.')
        
        



