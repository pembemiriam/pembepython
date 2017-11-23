def perfect(number):
	total=0
	for i in range(1,number):
		if(number%i==0):
			total=total+i
	return total
number=int(raw_input("enter a number:"))
if (number==perfect(number)):
    print "%d is a perfect number"	%(number)
else:
     print "%d is not a perfect number " %(number)  		






