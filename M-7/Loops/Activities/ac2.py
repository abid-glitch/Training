rows = int(input("enter number of rows"))
for r in range(rows):
    for s in range(r + 1):
        print("*", end=" ")
    print()
