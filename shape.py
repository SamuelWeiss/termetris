import random


LINE = 'line'
TEE = 'tee'
BLOCK = 'block'
LEFT_L = 'left_l'
RIGHT_L = 'right_l'
LEFT_S = 'left_s'
RIGHT_S = 'right_s'

all_shapes = [LINE, TEE, BLOCK, LEFT_S, RIGHT_S, LEFT_L, RIGHT_L]

class shape:

	def __init__(self):
		# choose randomly among shapes
		self.x = 5
		self.y = 1
		self.rotation = 0
		self.shape = random.choice(all_shapes)

	def __str__(self):
		res =  "I am a " + self.shape + ", my rotation is " + str(self.rotation) + " with position (" + str(self.x) + ", " + str(self.y)+ ", my coordinates are " + str(self.get_blocks())
		return res

	# HERE be dragons touch at your own risk
	def get_blocks(self):
		x = self.x
		y = self.y
		if self.shape == LINE:
			if self.rotation == 0 or self.rotation == 2:
				return [(x, y - 1), (x, y), (x, y + 1), (x, y + 2)]
			else:
				return [(x - 1, y), (x, y), (x + 1, y), (x + 2, y)]
		elif self.shape == TEE:
			if self.rotation == 0:
				return [(x - 1, y), (x, y), (x + 1, y), (x, y + 1)]
			elif self.rotation == 1:
				return [(x, y - 1), (x, y), (x, y + 1), (x + 1, y)]
			elif self.rotation == 2:
				return [(x - 1, y), (x, y), (x + 1, y), (x, y - 1)]
			else:
				return [(x, y - 1), (x, y), (x, y + 1), (x - 1, y)]
		elif self.shape == BLOCK:
			return [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]
		elif self.shape == LEFT_L:
			if self.rotation == 0:
				return [(x, y), (x, y - 1), (x - 1, y + 1), (x, y + 1)]
			elif self.rotation == 1:
				return [(x, y), (x - 1, y), (x - 1, y - 1), (x + 1, y)]
			elif self.rotation == 2:
				return [(x, y), (x, y - 1), (x + 1 , y - 1), (x, y + 1)]
			else:
				return [(x, y), (x + 1, y), (x + 1, y + 1), (x - 1, y)]
		elif self.shape == RIGHT_L:
			if self.rotation == 0:
				return [(x, y), (x, y - 1), (x + 1, y + 1), (x, y + 1)]
			elif self.rotation == 1:
				return [(x, y), (x - 1, y), (x - 1, y + 1), (x + 1, y)]
			elif self.rotation == 2:
				return [(x, y), (x, y - 1), (x - 1 , y - 1), (x, y + 1)]
			else:
				return [(x, y), (x + 1, y), (x + 1, y - 1), (x - 1, y)]
		elif self.shape == RIGHT_S:
			if self.rotation == 0 or self.rotation == 2:
				return [(x, y), (x + 1, y), (x , y + 1), (x - 1, y + 1)]
			elif self.rotation == 1 or self.rotation == 3:
				return [(x, y), (x, y + 1), (x - 1, y), (x - 1, y - 1)]
		elif self.shape == LEFT_S:
			if self.rotation == 0 or self.rotation == 2:
				return [(x, y), (x - 1, y), (x , y + 1), (x + 1, y + 1)]
			elif self.rotation == 1 or self.rotation == 3:
				return [(x, y), (x, y + 1), (x + 1, y), (x + 1, y - 1)]


	def rotate_right(self):
		self.rotation += 1 
		print self.rotation
		self.rotation = self.rotation % 4
		print self.rotation

	def rotate_left(self):
		self.rotation += 3 
		self.rotation = self.rotation % 4

	def translate_x(self, amount):
		self.x = self.x + amount

	def translate_y(self, amount):
		self.y = self.y + amount

	def get_shape(self):
		return self.shape

	def get_pretty_shape(self):
		if self.shape == LINE:
			return " #\n #\n #\n #\n"
		elif self.shape == BLOCK:
			return "\n ##\n ##\n\n"
		elif self.shape == TEE:
			return "\n #\n###\n\n"
		elif self.shape == LEFT_L:
			return "  #\n  #\n ##\n\n"
		elif self.shape == RIGHT_L:
			return "  #\n  #\n  ##\n\n"
		elif self.shape == LEFT_S:
			return "\n##\n ##\n\n"
		elif self.shape == RIGHT_S:
			return "\n ##\n##\n\n"
		else:
			return ""

	def reset_position(self):
		self.x = 5
		self.y = 1
		self.rotation = 0