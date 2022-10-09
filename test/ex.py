class User():
    def __init__(self,nick,gmail,password,first_name,last_name):
        self.nick = nick
        self.gmail = gmail
        self.password = password
        self.name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def Describe_user(self):
        print(f"{self.nick},{self.gmail},{self.password},{self.name},{self.last_name}")
    def Greet_user(self):
        print(f"Добро пожаловать {self.name} {self.last_name}")
    def Increment_login_attempts(self):
        self.login_attempts += 1
    def Reset_login_attempts(self):
        self.login_attempts = 0
class Admin(User):
    def __init__(self,nick,gmail,password,first_name,last_name):
        super(Admin, self).__init__(nick,gmail,password,first_name,last_name)
        self.privileges = []
    def Show_privileges(self):
        for privilegy in self.privileges:
            print(f"Ваши привилегии: {privilegy}")

admin1 = Admin("farer","farer@gmail.com","463rye46","Victor","Kunichin")
admin1.privileges.append("банить пользователей")
admin1.privileges.append("просматривать и удалять чат")
user1 = User("rob","rob432@gmai.com","5421bnds7","Albert","Chugunov")
user2 = User("crash","crash567@gmail.com","421gd61st","Danya","Holopov")
user1.Describe_user()
user1.Greet_user()
user1.Increment_login_attempts()
admin1.Show_privileges()
print(user1.login_attempts)
user1.Reset_login_attempts()
print(user1.login_attempts)
user2.Greet_user()
user2.Describe_user()
