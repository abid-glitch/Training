class Bird:
    def __init__(self, bird_name, bird_age):
        self.name = bird_name
        self.age = bird_age

    def sing(self, music):
        return "{} is singing {}".format(self.name, music)

    def dance(self):
        return "{} started dancing".format(self.name)

bird = Bird("Blu", 10)
print(bird.sing("‘Happy’"))
print(bird.dance())
