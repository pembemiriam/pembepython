number=raw_input("enter a 5 digit number")
num=int(number)
a=num/10000
b=num%10000
c=b/1000
d=b%1000
e=d/100
f=d%100
g=f/10
h=f%10
if (a==h):
	if (c==g):
		print '%d is a palindrome' %(num)
else:
     print '%d is not a palindrome'	%(num)	