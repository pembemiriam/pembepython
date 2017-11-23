import math
import random
def guess():
	random.seed()
	number1=random.randrange(0,1000)
	print(number1)
	while (1):
		y=1

		number=int(raw_input("guess the number\n"))
		if number1==number:
		    print "excellent, you guessed the number!"
		    break

		elif(number>number1):
		    print"too high"
		    pass

		else:
		    print"too low" 

	question=int(raw_input("would u want to continue(yes=1,no=2)?\n"))

	if (question==1): 
		guess()
	else:
		print 'thank u'
                                                                                                                                 

guess()



