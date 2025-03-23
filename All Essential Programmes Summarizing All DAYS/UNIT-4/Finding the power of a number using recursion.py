def power(base, exp):
    return 1 if exp == 0 else base * power(base, exp - 1)

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print("Result:", power(base, exp))
