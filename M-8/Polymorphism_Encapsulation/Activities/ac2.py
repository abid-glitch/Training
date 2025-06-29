class Computer:

    def __init__(self):
        self.__price = 900

    def sell(self):
        print("Selling Price: {}".format(self.__price))

    def set_price(self, value):
        self.__price = value

device = Computer()
device.sell()

device.__price = 1000
device.sell()

device.set_price(1000)
device.sell()
