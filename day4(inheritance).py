# OOP- PYTHON: INHERITANCE

class Pet:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    
    def show(self):
        print(f"i am {self.name} and i am {self.age} years old")

class Cats(Pet):
    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.colour= colour

    def speak(self):
        print("meow!")

    def show(self):
        print(f"i am {self.name} and i am {self.age} years old and i am {self.colour}.")

class Dogs(Pet):
    def speak(self):
        print("woof!!")

c1= Cats("jill", 5, "ginger")
c1.show()
c1.speak()

d1=Dogs("musky", 3)
d1.show()