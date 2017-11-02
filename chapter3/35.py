num=raw_input("enter a binary number:")
numb=int(num)
n=0
total=0
for i in num:
   print 'i is',i
   a=i*2**n
   print 'value is',a
   b=int(a)
   n=n+1
   val=b+total
   total=val
print 'the decimal is',val	