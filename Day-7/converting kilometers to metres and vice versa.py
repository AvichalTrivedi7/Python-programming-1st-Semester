choice=input("Please specify if you want to convert kilometres to metres (Enter 1) or metres to kilometres (Enter 2): ")

if choice=="1":

    kilometers=float(input("Enter distance in kilometers: "))

    conversion_factor=1000

    metres=kilometers*conversion_factor

    print(f"{kilometers} kilometers is equal to {metres} metres")

if choice=="2":

    metres=float(input("Enter distance in metres: "))

    conversion_factor=1000

    kilometres=metres/conversion_factor

    print(f"{metres} metres is equal to {kilometres} kilometres")

else:

    print("You entered the wrong choice, please choose between 1 and 2")
