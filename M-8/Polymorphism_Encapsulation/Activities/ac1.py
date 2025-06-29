class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, dog_name, dog_age):
        self.name = dog_name
        self.age = dog_age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


a = Cat("Dodo", 2.5)
b = Dog("Tyson", 8)

for pet in (a, b):
    pet.make_sound()
    pet.info()
