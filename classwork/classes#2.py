class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def change_password(self):
        new_password = input('Please create new password\n')
        self.password = new_password

    def get_username(self):
        print(f'username: {self.username}')

    def get_email(self):
        print(f'email: {self.email}')
    
    def show_password(self):
        print(f'password: {self.password}')

class Client(User):
    def __init__(self, username, password, email, name, surname, address):
        super().__init__(username, password, email)
        self.name = name
        self.surname = surname
        self.address = address

    def full_info(self):
        print('See client information as per your request below')
        print(f'username: {self.username}\npassword: {self.password}\nemail: {self.email}\nname: {self.name}\nsurname: {self.surname}\naddres: {self.address}')


class VIP(Client):
    def __init__(self, username, password, email, name, surname, address, type):
        super().__init__(username, password, email, name, surname, address)
        self.type = type 

    def change_type(self):
        new_type = input('Do you want to change type?\n')
        if new_type == 'yes':
            choose_new_type = input('Please choose new type\n')
            self.type = choose_new_type
        else:
            self.type = type 

    def show_info(self):
        print('See VIP client information as per your request below')
        print(f'username: {self.username}\npassword: {self.password}\nemail: {self.email}\nname: {self.name}\nsurname: {self.surname}\naddres: {self.address}\ntype: {self.type}')


class Manager(User):
    def __init__(self, username, password, email, name, surname, department):
        super().__init__(username, password, email)
        self.deprtmanet = department
        self.name = name
        self.surname = surname
        self.department = department

    def show_info(self):
        print('See manager information as per your request below')
        print(self.username)
        print(self.password)
        print(self.email)
        print(self.name)
        print(self.surname)
        print(self.department)
    
    def check_client(self):
        client.full_info()
        vip_client.show_info()

    def give_discount(self):
        print('This client will have 15% discount')

class Senior(Manager):
    def __init__(self, username, password, email, name, surname, department, position):
        super().__init__(username, password, email, name, surname, department)
        self.position = position

    def show_info(self):
        print('See Senior information as per your request below')
        print(self.username)
        print(self.password)
        print(self.email)
        print(self.name)
        print(self.surname)
        print(self.department)
        print(self.position)

user = User('danatjie', '12345', 'dana@gmmail.com')  
client = Client('asselt', '123asd', 'assel@gmmail.com', 'Assel', 'Tussupbekova', 'Pavlodar')
vip_client = VIP('ainash', '123qwe', 'ainash@gmmail.com', 'Ainash', 'Jussupova', 'Pavlodar', 'VIP')
manager = Manager('danatjie', '12345', 'dana@gmmail.com', 'Dana', 'Khamza', 'Asset Management')
senior = Senior('fernandof', '123543', 'flores@gmmail.com', 'Fernando', 'Flores', 'Asset Management', 'Asset Manager')


manager.give_discount()
