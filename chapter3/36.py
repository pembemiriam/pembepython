n=raw_input("enter a non negative integer:")
a=int(n)
total=1
if (a==0):
	print 'the factorial is 1'
elif(a<0):
	print'the factorial of a negative number does not exist'
else:	
	while (a>1):
		fact=a*(a-1)
		a=a-2
		total=fact*total
	print 'the factorial is', total

    	