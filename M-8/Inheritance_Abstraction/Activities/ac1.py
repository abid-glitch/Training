class Individual(object):

    def __init__(self, full_name, uid):
        self.full_name = full_name
        self.uid = uid

    def show(self):
        print(self.full_name)
        print(self.uid)

class Staff(Individual):

    def __init__(self, full_name, uid, pay, role):
        self.pay = pay
        self.role = role
        Individual.__init__(self, full_name, uid)

b = Staff('Penguin', 20210401, 15000, "Intern")
b.show()
