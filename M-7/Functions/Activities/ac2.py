def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)

val = int(input("Enter a number: "))

if val < 0:
    print("Sorry, factorial doesn't exist for negatives")
elif val == 0:
    print("The factorial of 0 is 1")
else:
    print("Factorial of", val, "is", factorial_recursive(val))
