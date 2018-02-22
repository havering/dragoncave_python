import rooms

def initialize_rooms():
	# jewels, weapons, weapon_name, room_name, room_desc, room_id):

	rooms = []
	
	desc = "You find yourself deep in catacombs. The light from the entrance is dim and \nfar away, but bright enough for you to follow."
	first = Room(0, 0, None, "a deep cave", desc, 1)
	rooms.append(first)

	desc = """
			As the light grows brighter, your eyes are caught by the gleam of metal and \njewels in the corner. \n
			A small pile of rubies sits on a rough rock ledge, \nwhile a dagger rests on the floor beneath.
		   """
	second = Room(3, 1, "a dagger", "a dimly lit cave", )