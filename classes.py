class Room:
	# attributes
	def __init__(self, jewels, weapons, weapon_name, room_name, room_desc, room_id, north, south, east, west):
		self.jewels = jewels # int
		self.weapons = weapons #int
		self.weapon_name = weapon_name # string
		self.room_name = room_name # string
		self.room_desc = room_desc # string
		self.room_id = room_id # int
		self.north = north # Room
		self.south = south # Room
		self.east = east # Room
		self.west = west # Room


class Player:
	# attributes
	def __init__(self):
		self.moves = 0
		self.jewels = 0
		self.weapons = 0
		self.puzzle1 = false
		self.puzzle2 = false
		self.puzzle3 = false
		self.weapon_names = []

class Map:
	# attributes
	def __init__(self, starter, ender):
		self.start = starter # Room
		self.end = ender # Room
