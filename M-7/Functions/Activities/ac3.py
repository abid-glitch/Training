def sum_vals(a, b):
    return a + b

def diff_vals(a, b):
    return a - b

def prod_vals(a, b):
    return a * b

def div_vals(a, b):
    return a / b

n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))

print("Sum is:", sum_vals(n1, n2))
print("Difference is:", diff_vals(n1, n2))
print("Product is:", prod_vals(n1, n2))
print("Quotient is:", div_vals(n1, n2))
