n = int(input("Enter a number: "))
temp = n
arm = 0
order = len(str(n))

while temp > 0:
    digit = temp % 10
    arm += digit ** order
    temp //= 10

if arm == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
