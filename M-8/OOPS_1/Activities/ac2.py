class Student:
    grade = 10
    name = "Penguin"

    def intro(self):
        print("Hello, I am a learner")

    def info(self):
        print("My name's", self.name)
        print("Currently in Grade", self.grade)

obj = Student()
obj.intro()
obj.info()
