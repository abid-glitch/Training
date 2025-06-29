from abc import ABC, abstractmethod

class Creature(ABC):
    def move(self):
        pass

class Person(Creature):
    def move(self):
        print("I can walk and run")

class Reptile(Creature):
    def move(self):
        print("I can crawl")

class Pup(Creature):
    def move(self):
        print("I can bark")

class CatKing(Creature):
    def move(self):
        print("I can roar")

obj1 = Person()
obj1.move()

obj2 = Reptile()
obj2.move()

obj3 = Pup()
obj3.move()

obj4 = CatKing()
obj4.move()
