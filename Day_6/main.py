class Dog:

    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Wof")

class Owner:
    def __init__(self,name,address,number):
        self.name = name
        self.address = address
        self.number = number

owner1 = Owner("James","USA","123-456")
owner2 = Owner("Clara","China","654-123")

dog1 = Dog("Arthur","Golden",owner1)
print(dog1.name,dog1.breed,dog1.owner.name,dog1.owner.address,dog1.owner.number)
dog1.bark()

dog2 = Dog("Benny","Chihuahua",owner2)
dog2.bark()





