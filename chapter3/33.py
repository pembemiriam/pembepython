
grade1=counter=0
gallon=raw_input("enter the gallons used (-1 to end) :")
gallo=int(gallon)
while(gallo !=-1):
	miles=raw_input("enter the miles driven")
	mile=int(miles)
	total=mile/gallo
	grade=total+grade1
	grade1=grade
	counter=counter + 1
	print 'the miles / gallon is',total
	gallon=raw_input("enter the gallons used (-1 to end) :")
	gallo=int(gallon)
print 'grade is',grade
print 'counter is',counter
av=grade/counter
print 'the overall average miles per gallon was is', av