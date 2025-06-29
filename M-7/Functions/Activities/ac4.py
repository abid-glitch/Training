def add_vals(p, q):
    return p + q

def sub_vals(p, q):
    return p - q

def mul_vals(p, q):
    return p * q

def div_vals(p, q):
    return p / q

value1 = int(input("Enter Number 1: "))
value2 = int(input("Enter Number 2: "))

print("Addition:", add_vals(value1, value2))
print("Subtraction:", sub_vals(value1, value2))
print("Multiplication:", mul_vals(value1, value2))
print("Division:", div_vals(value1, value2))
