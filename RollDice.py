import random
import time

#Bool variable
roll_again = "yes"

#roll dice until user doesn't want to play
while roll_again == "yes" or roll_again == "y" or roll_again == "Yes" or roll_again == "Y" or roll_again == "YES":
	print("\nRolling the dice...")
	#pause the code so that it feels like dice is being rolled
	#sleep 1 second
	time.sleep(1)
	
	#pick variable between 1 and 6
	dice1=random.randint(1, 6)
	dice2=random.randint(1, 6)
	
	print("The values are:")
	print("Dice 1 =", dice1, "Dice 2 =", dice2)
	
	if dice1 == dice2:
		print("You rolled a double")
	else: 
		print("Keep trying!")
		
	#option to change yes to no	
	roll_again = input("\nRoll the dice again? (Y/N) ")
	