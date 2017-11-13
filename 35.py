num=raw_input("enter a binary number:")
numb=int(num)
n=10
t=0
total=0
while (numb!=0):
   n=10
   a=numb/n
   b=numb%n
   c=b*2**t
   numb=a
   t=t+1
   val=c+total
   total=val
print 'the decimal is',val	