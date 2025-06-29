class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def display_name(self):
        print(self.first, self.last)

class Learner(Person):
    def __init__(self, first, last, grad_year):
        super().__init__(first, last)
        self.grad_year = grad_year

p = Learner("Joey", "King", 2021)
p.display_name()
print(p.grad_year)
