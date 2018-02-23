import initialize
import classes
from random import randint

def play_game(game_map):
	current = game_map.start

	dude = classes.Player()

	see_menu()

	while (current != game_map.end):
		# one move per loop 
		# additional moves added for attempts at solving puzzles
		dude.moves += 1

		print "\nYou find yourself in %s." % current.room_name
		print current.room_desc
		print "\n"

		# puzzle rooms
		if (current.room_id == 3):
			if (dude.puzzle1):
				print "You have already solved this puzzle, so you are free to go about your business."
			else:
				num_moves = game_one()
				dude.moves += num_moves
				dude.puzzle1 = True

		if (current.room_id == 5):
			if (dude.puzzle2):
				print "You have already solved this puzzle, so you are free to go about your business."
			else:
				num_moves = game_two()
				dude.moves += num_moves
				dude.puzzle2 = True

		if (current.room_id == 9):
			if (dude.puzzle3):
				print "You have already solved this puzzle, so you are free to go about your business."
			else:
				num_moves = game_three()
				dude.moves += num_moves
				dude.puzzle3 = True

		# no option to collect jewels in the dragon's opening
		if (current.room_id == 10):
			dragon_room(dude)
		else:
			answer = raw_input("Would you like to gather jewels (1), keep a weapon (2), or move on (3)? ")

			while (int(answer) < 1 or int(answer) > 3):
				answer = raw_input("Try again, using an integer between 1 and 3: ")

			if (int(answer) == 1):
				if (current.jewels > 0):
					print "You pick out %i jewels and decide to move on." % current.jewels
					dude.jewels += current.jewels
				else:
					print "Unfortunately, there are no jewels to be found. You decide to move on."

			if (int(answer) == 2):
				if (current.weapons > 0):
					print "You pick out %i weapon, %s, and keep moving." % (current.weapons, current.weapon_name)
					dude.weapons += current.weapons
					dude.weapon_names.append(current.weapon_name)
				else:
					print "Unfortunately, there are no weapons to be found. You decide to move on."

			if (int(answer) == 3):
				print "There's nothing of interest here. Better keep moving."

		# directional choices
		print "Which direction would you like to go?"
		print "\t1. North"
		print "\t2. South"
		print "\t3. East"
		print "\t4. West"
		answer = raw_input("Enter a choice: ")

		while (int(answer) < 1 or int(answer) > 4):
			answer = raw_input("Invalid entry. Choose between 1 and 4: ")

		if (int(answer) == 1):
			if (current.north == None):
				print "You feel along the northern wall, but can't find an opening."
			else:
				print "You leave to the north."
				current = current.north

		if (int(answer) == 2):
			if (current.south == None):
				print "You feel along the southern wall, but can't find an opening."
			else:
				print "You leave to the south."
				current = current.south

		if (int(answer) == 3):
			if (current.east == None):
				print "You feel along the eastern wall, but can't find an opening."
			else:
				print "You leave to the east."
				current = current.east

		if (int(answer) == 4):
			if (current.west == None):
				print "You feel along the western wall, but can't find an opening."
			else:
				print "You leave to the west."
				current = current.west

		if (current == game_map.end):
			print "You find yourself in %s." % current.room_name
			print current.room_desc
			exit()




def see_menu():
	print "Would you like to see the goal of the game?"
	answer = raw_input("Use 1 for yes or 2 for no: ")

	while (int(answer) < 1 or int(answer) > 2):
		answer = raw_input("Try again. 1 for yes or 2 for no: ")

	if int(answer) == 1:
		print "********************************************************************"
		print "*          The goal of the game is to escape the cave.             *"
		print "*  You must gather enough items to move past the final challenge.  *"
		print "* You may go back and gather more items if you do not have enough. *"
		print "********************************************************************"


# guess the correct number between 1 and 4
def game_one():
	num_tries = 1
	master = randint(1, 4)

	print "The troll swings the ax over his shoulder and eyes you smugly. 'I'm thinking of"
	print "a number between 1 and 4,' he says. 'If you can guess the number, you can pass.'"
	answer = raw_input("That's it? It could be worse. Time to tell him your number: ")

	while (int(answer) < 1  or int(answer) > 4):
		answer = raw_input("Hint: enter a number between 1 and 4: ")

	while (int(answer) != master):
		num_tries += 1

		print "'Wrong!' The troll is almost giddy. 'Try again, or you'll never get out.'"
		answer = raw_input("You think of another number to tell him: ")

		while (int(answer) < 1  or int(answer) > 4):
			answer = raw_input("Hint: enter a number between 1 and 4: ")

	if (int(answer) == master):
		print "The troll seems shocked that you have guess correctly, but begrudgingly"
		print "lets you pass."

		return num_tries

# riddle
def game_two():
	num_tries = 1
	answer = 'e'

	print "Sensing your agreement, the magical voice hums again in your head:"
	print "   I am the beginning of the end, the end of every place."
	print "   I am the beginning of eternity, the end of time and space."
	print "   What am I?\n"
 	guess = raw_input("Hmmm, what is your guess? ")

 	while (guess.lower() != answer):
 		num_tries += 1
 		print "A loud buzz vibrates inside your head. 'Incorrect,' the voice hums."
 		print "(Hint: enter an alphabetical character)"
 		guess = raw_input("You try to think of another guess: ")

 	if (guess.lower() == answer):
 		print "The magical voice's approval is warm and bright, if such a thing can"
 		print "be said about a telepathic presence. 'Correct!' The lock on the chest"
 		print "falls open, revealing jewels and a weapon inside."

 		return  num_tries

 # random guessing game
def game_three():
 	num_tries = 1

 	print "The serpent weaves back and forth between you and the next part of the cave."
 	print "'Answer this: what lies beyond me in this cave?'"
 	print "\t1. A dragon"
 	print "\t2. A potato"
 	print "\t3. A birdhouse\n"

 	guess = raw_input("Which is it? ")

 	while (int(guess) < 1 or int(guess) > 3):
 		num_tries += 1
		guess = raw_input("(Hint: enter an integer between 1 and 3) ")


 	while (int(guess) != 1):
 		num_tries += 1
		guess = raw_input("The serpent hisses disapproval. 'Falsssssse. Try again.' ")


	if (int(guess) == 1):
 		print "'Yesssss, you are correct,' the serpent hisses. 'You may passsssss.'"
 		return num_tries

# player chooses to fight the dragon, gather more supplies, or bribe the dragon
# if the player has taken too many turns, they automatically lose and die
def dragon_room(dude):
	if (dude.moves > 20):
		print "Oh no! The dragon is out of patience. He lets out a might roar and"
		print "burns you to a crisp.\n"
		print "                  GAME OVER                   "
		exit()
	else:
		answer = raw_input("Do you try to bribe the dragon (1), fight the dragon (2),\nor go back to gather supplies (3)? ")

		while (int(answer) < 1 or int(answer) > 3):
			answer = raw_input("Try again, using an integer between 1 and 3: ")

		if (int(answer) == 1):
			# user must have 15 jewels to bribe the dragon
			print "You rummage in your bag for the jewels you have stashed."
			print "You have %i jewels to offer." % dude.jewels
			print "You hold them out to the dragon and hold your breath."

			if (dude.jewels >= 15):
				print "The dragon growls deep in its throat, but gently swipes the pile of jewels\nout of your hands."
				print "Success! The opening is left clear, and you are free to leave the cave."
				return
			else:
				print "The dragon yawns widely at you, flames escaping its maw as it does so."
				print "It seems do you do not have enough jewels to bribe him. Better head back to the cave."
				return

		if (int(answer) == 2):
			# user must have 5 weapons to fight the dragon
			print "Finally, these heavy weapons come in handy!"
			print "You peer inside your bag - you have "
			for item in dude.weapon_names:
				print item + ", ", 
			print "and your wits about you."

			if (dude.weapons >= 5):
				print "The dragon roars as it sees your available arsenal. It gives you a scathing\n look, and slinks out of the way."
				print "That was anticlimatic."
				return
			else:
				print "The dragon threatens you with little snorts of flame, and you suddenly"
				print "realize that you aren't armed well enough to take on a battle."
				print "Perhaps you should head back into the cave for more supplies ..."
				return

		if (int(answer) == 3):
			print "You decide to slip back and gather more supplies to help you make your choice."
			return

def main():
	game_map = initialize.initialize_rooms()

	# print "Game map has initialized!"

	play_game(game_map)



main()