a=raw_input("enter an interger:")
a=int(a)
b=raw_input("enter another integer:")
b=int(b)
c=a%b
if (c==0):
 print '%d is a multiple of %d '%(a,b)
else:
	print '%d is not a multiple of %d' %(a,b)