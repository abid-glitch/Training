x_val = 5
y_val = 9
z_val = 1

print("Before swapping :")
print("x =", x_val)
print("y =", y_val)
print("z =", z_val)

backup = z_val
z_val = y_val
y_val = x_val
x_val = backup

print("\nAfter swapping :")
print("x =", x_val)
print("y =", y_val)
print("z =", z_val)
