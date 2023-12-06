import json

data = {'Dana.T': {'password': 'asd123', 'name': 'Dana', 'type': 'student'}, 
'Assel.T': {'password': '123qwe', 'name': 'Assel', 'type': 'student'}, 
'Dilda.K': {'password': 'qwe123', 'name': 'Dilda', 'type': 'teacher'}}

with open('assignment4.json', 'w') as file:
    json.dump(data, file, indent=2)


class System:
    def __init__(self):
        def self.start():
            while True:
                system_choice = input('1)Login\n2)Sign up\n')
                if system_choice == 1:
                    log_in()
                if system_choice == 2:
                    sign_up()


    
system = System()