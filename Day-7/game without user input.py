import random

flag=0

a=random.randint(1,100)
while True:

    b=random.randint(1,100)

    if a==b:

        print("You won")

        break

    else:

        flag+=1

print(f"You lost {flag} time(s) before winning")
