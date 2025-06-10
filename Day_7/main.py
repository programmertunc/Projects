class User:
    def __init__(self,username,email ,password):
        self._username = username
        self._email = email
        self._password = password
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,new_email):
        self._email = new_email
"""
user1 = User("Daniel","daniel@",123)
user1.email = "aqsdqw"
print(user1.email)
"""
"""
    def get_username(self):
        return self._username
    def set_username(self,username):
        self._username = username

    def get_email(self):
        return self._email
    def set_email(self,email):
        self._email = email
    
    def get_password(self):
        return self._password
    def set_password(self,password):
        self._password = password
"""

   
class Person:
    person_count = 0
    def __init__(self,name):
        self._name = name
        Person.person_count += 1
        
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

person1 = Person("James")
print(Person.person_count)

person2 = Person("Ally")
print(Person.person_count)

    
