tup = ()
print(tup)

tup = (1, 2, 3)
print(tup)

tup = (1, "Hello", 3.4)
print(tup)

tup = ("mouse", [8, 4, 6], (1, 2, 3))
print(tup)

tup = ('p','e','r','m','i','t')
print(tup[0])
print(tup[5])

nested = ("mouse", [8, 4, 6], (1, 2, 3))
print(nested[0][3])
print(nested[1][1])

print("Sliced :", tup[1:4])

for item in tup:
    print("Hello", item)
