def fahrenheit (number):
  a=1.8
  F=float((a*number)+32)
  return F
for celcius in range(0,101):
  print "the fahrenheit of %2d is %3.1f" %(celcius,fahrenheit(celcius))
