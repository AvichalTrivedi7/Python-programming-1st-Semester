def is_Prime(num):
	if num<=1:
		return False
	if num<=3:
		return True
	i=5
	while i*i<=num:
		if num%i==0 or num%(i+2)==0:
			return False
		i+=6
	return True

number=int(input("Please enter the number you want to check for prime: "))
if is_Prime(number):
    print(f"This number {number} is prime")
else:
    print(f"This number {number} is not prime")
