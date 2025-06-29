class Bird:
    species = "bird"

    def __init__(self, bird_name, bird_age):
        self.name = bird_name
        self.age = bird_age

bird1 = Bird("Blu", 10)
bird2 = Bird("Woo", 15)

print("Blu belongs to", bird1.species)
print("Woo is also a", bird2.species)

print("{} has lived for {} years".format(bird1.name, bird1.age))
print("{} has lived for {} years".format(bird2.name, bird2.age))
