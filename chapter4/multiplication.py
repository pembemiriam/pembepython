import math
import random
def multiply():
	
	random.seed()
	number1=random.randint(1,10)
	number2=random.randint(1,10)
	result=int(number1*number2)
	guess=int(raw_input("what is"+str(number1)+"x"+str(number2)+"?"))
	while(1):
		print(result)
		if (guess==result):
			print "correct answer"
			break
		else:
			print "wrong answer"
			guess=int(raw_input("what is"+str(number1)+"x"+str(number2)+"?"))
			
		
		     
		
		
	
		

multiply()		



				
				
				
				    
				
		
		
		
		

		    


	   
	

