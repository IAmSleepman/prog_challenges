import random

RPS = ["Rock", "Papers", "Scissors"]
Player_Choice = input("Choice your sign: ")
Random_Choice = random.choice(RPS)
print("Opponent choices", Random_Choice)
if Player_Choice == "Rock":
	if Random_Choice == "Papers":
		print ("You Lose.")
	elif Player_Choice == Random_Choice:
		print ("Tie")	
	else:
		print ("You're Winner.")
elif Player_Choice == "Papers":
	print(Random_Choice)
	if Random_Choice == "Scissors":
		print ("You Lose.")
	elif Player_Choice == Random_Choice:
		print ("Tie")	
	else:
		print ("You're Winner.")
else:
	if Random_Choice == "Rock":
		print ("You Lose.")
	elif Player_Choice == Random_Choice:
		print ("Tie")	
	else:
		print ("You're Winner.")
