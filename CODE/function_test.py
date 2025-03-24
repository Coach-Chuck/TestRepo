# def catCounter():
# 	d=1
# 	print(d)

# catCounter()


# Define the function named ageGame
def ageGame():
# Assign the veriable age to the value inputed on the terminal
	age = input ("How old is Coach Chuck? ")
# input() is assigned as a string	
	if age == "33":
		print(age+ " years old. You're correct")
# int() converts a string to interger
	elif  int(age)<33:
		print (age + " years old? Too young, nice try")
		ageGame()
	else:
		print (age + " years old? Too old, nice try")		
		ageGame()
#run the function
ageGame()

# def colorGame():
# 	color=input("What is Coach Chuck's favorite color? ")
# 	if color!= "green":
# 		if color=="hint":
# 			print("Coach Chuck loves the outdoors")
# 			colorGame()
# 		else:
# 			print("Nope, try again")
# 			colorGame()
# 	else:
# 		print("You're right")
# colorGame()

