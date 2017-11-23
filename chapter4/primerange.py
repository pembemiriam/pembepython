def prime(number1):
	prime = True
	for i in range(2,number1):
		if (number1%i==0):
			prime = False
	if prime:
		print "%d is a prime" %(number1)

for i in range(2,10001):

 
    prime(i)   