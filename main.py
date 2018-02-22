# import rooms
import initialize
import classes

def play_game(game_map):
	current = game_map.start

	dude = classes.Player()

	see_menu()



def see_menu():
	print "Would you like to see the goal of the game?"
	answer = raw_input("Use 1 for yes or 2 for no: ")

	print "answer is %s" % answer

	while (answer < 1 and answer > 2):
		answer = raw_input("Try again. 1 for yes or 2 for no: ")

	if int(answer) == 1:
		print "********************************************************************"
		print "*          The goal of the game is to escape the cave.             *"
		print "*  You must gather enough items to move past the final challenge.  *"
		print "* You may go back and gather more items if you do not have enough. *"
		print "********************************************************************"



def main():
	game_map = initialize.initialize_rooms()

	# print "Game map has initialized!"

	play_game(game_map)



main()