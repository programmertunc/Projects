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
person1 = Person("Andy",29)
person1.greet()
person1.walk()

person1.change_name("Mandy")
person1.greet()


class User:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
    def greetUser(self,user):
        print(f"Hi {user.username} i am {self.username}")
user1 = User("Abby","abby@email.com","754afd")
user2 = User("Jonathan","jonathan@email.com","dfswerg")
user1.greetUser(user2)