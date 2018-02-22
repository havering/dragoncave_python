import classes

def initialize_rooms():
	# jewels, weapons, weapon_name, room_name, room_desc, room_id, north, south, east, west

	# rooms = []
	
	desc = "You find yourself deep in catacombs. The light from the entrance is dim and \nfar away, but bright enough for you to follow."
	first = classes.Room(0, 0, None, "a deep cave", desc, 1, None, None, None, None)
	# rooms.append(first)

	desc = """
			As the light grows brighter, your eyes are caught by the gleam of metal and \njewels in the corner. \n
			A small pile of rubies sits on a rough rock ledge, \nwhile a dagger rests on the floor beneath.
		   """
	second = classes.Room(3, 1, "a dagger", "a dimly lit cave", desc, 2, None, None, None, first)
	first.east = second

	desc = """
			You squeeze into the next catacomb, which is considerably narrower than the \nfirst. The exit is blocked by a squat troll, whose ax dissuades you from \npassing.
			'You can pass if you solve a puzzle,' the troll growls at you. \nYou have no choice but to agree.
		   """
	third = classes.Room(4, 1, "a helmet", "a narrow catacomb", desc, 3, first, None, None, None)
	second.south = third

	desc = """
			Your relief at making it past the gnome turns to delight as you find yourself \nin a new cavern.
		    This one is draped in velvet, fur, strings of jewelry, and \npiles of gold. Who would leave such riches laying about?
		   """

	fourth = classes.Room(5, 0, None, "an opulant room", desc, 4, None, None, third, None)
	third.west = fourth

	desc = """
			This room in the cave is not nearly so pleasant. It smells musty and is covered\nin thick cobwebs. You do your best to pick through them.
			As you step to the \nsideto avoid an intact web, your foot kicks up against a locked chest. You \ndon't see a key, but as you touch the lock, a voice hums in your mind:
			\n'Solve a riddle to gain a reward.'
		   """

	fifth = classes.Room(4, 1, "a mace", "a cobwebbed cave", desc, 5, fourth, None, None, None)
	fourth.south = fifth

	desc = "You enter what appears to be an armory. Racks and racks of swords, shields, and\nspears fill the large space. You consider grabbing one before moving on."
	sixth = classes.Room(0, 1, "a shield", "an armory", desc, 6, None, None, None, fifth)
	fifth.east = sixth

	desc = """
    		There are cockroaches everywhere. Your stomach churns, and you try to ignore \nthe crunching as you stride quickly across the room.
			\nThe gleam of metal and jewels again catches your eye - but it is tempting \nto move on without investigating.
		   """

	seventh = classes.Room(3, 1, "a throwing star", "a cave covered in cockroaches", desc, 7, None, None, None, sixth)
	sixth.east = seventh

	desc = """
    		The good news is that you've made it through the room full of cockroaches. The \nbad news is that the ceiling of this small cave is covered in bats.
			\n'Why don't they eat the cockroaches?' you wonder. A few of them stir when \nyou walk in, but for the most part, they seem to be asleep.
			\nYou are tempted by a satchel of jewels hanging from the hilt of a broadsword \nthat is leaned against the wall.
		   """

	eighth = classes.Room(3, 1, "a broadsword", "a cave filled with bats", desc, 8, None, seventh, None, None)
	seventh.north = eighth

	desc = """
    		The light from the entrance, which has been growing progressively brighter, \nbeams clearly into the room as you walk in. You freeze when you \nsee a serpent blocking your path. 
			The serpent raises its head and hisses \nat you, 'You musssst anssssswer a quessssstion iffff you want to esssscape.'
		   """
	ninth = classes.Room(4, 1, "a spear", "a bright room", desc, 9, None, None, None, eighth)
	eighth.east = ninth

	desc = """
    		You find yourself at the mouth of the cave. Just one problem: you find a dragon\nat the mouth of the cave, too. It rumbles at you, smoke curling up from its \nnostrils. 
		"You consider trying to dash past it, but there is not enough room \nfor you to squeeze past without being caught. You consider bribing or slaying \nthe dragon.
		   """

	tenth = classes.Room(0, 0, None, "the cave opening", desc, 10, None, ninth, None, None)
	ninth.north = tenth

	desc = "You did it! You've never been so relieved to see the sky."
	last = classes.Room(0, 0, None, "the open air", desc, 11, None, None, None, None)
	tenth.north = last

	game_map = classes.Map(first, last)

	return game_map
