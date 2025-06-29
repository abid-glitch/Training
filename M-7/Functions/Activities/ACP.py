def fib_recursive(x):
    if x <= 1:
        return x
    return fib_recursive(x - 1) + fib_recursive(x - 2)

terms = int(input("Enter Number of Terms: "))

if terms <= 0:
    print("Enter a number greater than 0")
else:
    print("Fibonacci Series:")
    for j in range(terms):
        print(fib_recursive(j))
