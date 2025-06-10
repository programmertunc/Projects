class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello my name is {self.name} i am {self.age} years old")
    def walk(self):
        print(f"{self.name} is walking")

    def change_name(self,name):
        self.name = name

"""
person1 = Person("Andy",29)
person1.greet()
person1.walk()

person1.change_name("Mandy")
person1.greet()
"""



class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email
        self.password = password
    def greetUser(self,user):
        print(f"Hi {user.username} i am {self.username}")

    def get_email(self):
        return self._email
    def set_email(self,email):
        self._email = email


user3 = User("Abigail","","123-123")
user3.set_email("abigail@email.com")
print(user3.get_email())