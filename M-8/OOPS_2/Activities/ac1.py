class Staff:

    def __init__(self):
        print('Staff created.')

    def __del__(self):
        print('Destructor triggered, Staff removed.')

person = Staff()
del person
