#homework4
login_data = {'Dana':{'password':'123asd'},
              'Assel':{'password':'321asd'}}

#1) open loop: login/logout or authorization
#2) do you have an account? yes/no/exit
# |if username exists: ask password
# ask the user if they have account
#3) if username and password are correct -> print ('You are logged in')
#4) log out
#5) back to 1)
#6) if no: create an account 
#7) please create username: unique username
#8) if username already in database ->('Please pick another username')
#9) password
#10) save data to login_data
#11) again 1


def log_in_account():
    while True:
        username = input('PLease enter your username ')
        
        if username in login_data:
            password = input('Please enter your password ')
            if password == login_data[username]['password']:
                print('You are logged in')
                break
            else:
                print('Incorrect password. Please try again.')
        else:
            print('Username not found. Please try again.')
            return
    
def create_account():
    create_account_choice = input('Do you want to create account? 1)Yes 2)No ')
    if create_account_choice == '1':
        unique_username = input('Please create unique username: ')
        if unique_username in login_data:
            print('Please pick another username')
            create_account()
        unique_password = input('Please create unique password: ')
        login_data[unique_username] = {'password': unique_password}
        print('Account created successfully.')
    elif create_account_choice == '2':
        print('fine')
        return

def exit_system():
    exit_system_choice = input('Do you want to exit system? 1)Yes 2)No ')
    if exit_system_choice == '1':
        print('bye')
    elif exit_system_choice == '2':
        return
    else:
        print('Invalid! Try 1 or 2')
        exit_system()
        return
        
while True:
    account_check = input('Do you have an account? 1)Yes 2)No 3)Exit ')
    if account_check == '3':
        exit_system()
    if account_check == '1':
        log_in_account()
    if account_check == '2':
        create_account()
    