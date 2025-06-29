s = {1, 2, 2, 3, 4, 4, 4}
print("Set :", s)

s.add(5)
print("Updated Set:", s)

a = s
b = {2, 4, 4, 6}

print("\nSet 1", a)
print("Set 2", b)
print("Difference")
print(a.difference(b))
print("Symmeteric Difference")
print(a.symmetric_difference(b))
