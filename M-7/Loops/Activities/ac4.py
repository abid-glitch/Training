check = int(input("Enter number to be checked :"))
is_prime = True

if check > 1:
    for x in range(2, check):
        if check % x == 0:
            is_prime = False
            break

if is_prime:
    print(check, "is a prime number")
else:
    print(check, "is not a prime number")
