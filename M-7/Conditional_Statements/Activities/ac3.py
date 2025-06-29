val = int(input("Enter a number to evaluate: "))

if val > 50:
    print("It is more than 50")
    if val % 2 == 0:
        print("It is also even")
    else:
        print("It is also odd")
else:
    print("It is less than or equal to 50")
