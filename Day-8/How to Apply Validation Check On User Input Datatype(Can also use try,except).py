num=input("Enter a number:")

if num.isdigit():


    num=int(num)


    if num>0:


        print("Positive number")


    elif num==0:


        print("Zero")


    else:


        print("Negative number")


elif num.isalnum():


    print("You've entered the wrong data")
    
    
