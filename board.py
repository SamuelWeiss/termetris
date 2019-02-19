import shape

class tetris_board:

	width = 10
	height = 21
	blocks = []

	def __init__(self):
		self.score = 0
		self.blocks = []
		for i in range(self.height):
			self.blocks.append([0] * self.width)

	def render_board(self, shape):
		self.look_for_complete_rows()
		# for row in self.blocks:
		# 	for block in row:
		# 		print block,
		# 		print " ",
		# 	print "\n",

		rendered_board = []
		# first render the blocks that are already in the board
		for row in self.blocks:
			rendered_row = []
			for block in row:
				if block == 1:
					rendered_row.append("#")
				else:
					rendered_row.append(" ")
			rendered_board.append(rendered_row)

		# now render where the piece could land (with stars)
		could_land_blocks = self.where_will_it_land(shape)
		for block in could_land_blocks:
			x = block[0]
			y = block[1]
			if y >= 0 and x >= 0:
				rendered_board[y][x] = "*"


		# finally render where the piece is now (so that we overwrite where it'll land)
		current_shape_blocks = shape.get_blocks()
		for block in current_shape_blocks:
			x = block[0]
			y = block[1]
			if y >= 0 and x >= 0:
				rendered_board[y][x] = "#"


		print "+" + ("-" * self.width) + "+"
		for row in rendered_board:
			print "|" + "".join(row)+ "|"
		print "+" + ("-" * self.width) + "+"


	def has_intersection(self, shape):
		shape_blocks = shape.get_blocks()
		for block in shape_blocks:
			# if you're above the board don't check!
			x = block[0]
			y = block[1]
			if y < 0:
				continue
			if x < 0:
				return True
			if x >= self.width:
				return True
			if (y >= self.height):
				return True
			if self.blocks[y][x] == 1:
				return True
				exit(1)
		return False


	def put_shape_in_board(self, shape):
		shape_blocks = shape.get_blocks()
		for block in shape_blocks:
			x = block[0]
			y = block[1]
			self.blocks[y][x] = 1


	def where_will_it_land(self, shape):
		# returns an array of locations where the shape will land
		fallen = 0
		while self.has_intersection(shape) == False:
			shape.translate_y(1)
			fallen += 1
		# move back up one
		shape.translate_y(-1)
		blocks = shape.get_blocks()
		shape.translate_y(-1 * (fallen - 1))
		return blocks


	def fall_shape(self, shape):
		shape.translate_y(1)
		if self.has_intersection(shape):
			shape.translate_y(-1)
			print "putting shape in board after finding an intersection "
			self.put_shape_in_board(shape)
			return None
		return shape


	def drop_shape(self, shape):
		while shape is not None:
			shape = self.fall_shape(shape)
		return None

	def fix_intersections(self, shape):

		#TODO: don't allow pieces to move outside the board

		if not self.has_intersection(shape):
			return shape

		shape.translate_x(1)
		if not self.has_intersection(shape):
			return shape
		shape.translate_x(-1)

		shape.translate_x(-1)
		if not self.has_intersection(shape):
			return shape
		shape.translate_x(1)

		shape.translate_y(-1)
		if not self.has_intersection(shape):
			return shape
		shape.translate_y(-1)
		return shape # TODO: there could be edge cases here that I do not see

	def rotate_shape_right(self, shape):
		# rotate the shape
		shape.rotate_right()
		self.fix_intersections(shape)
		return shape

	def rotate_shape_left(self, shape):
		shape.rotate_left()
		self.fix_intersections(shape)
		return shape

	def move_shape_left(self, shape):
		shape.translate_x(-1)		
		self.fix_intersections(shape)
		return shape

	def move_shape_right(self, shape):
		shape.translate_x(1)
		self.fix_intersections(shape)
		return shape

	def look_for_complete_rows(self):
		num_complete = 0
		# go backwards to not miss rows
		for index in xrange(self.height-1 , 0, -1):
			row = self.blocks[index]
			if sum(row) == self.width:
				num_complete += 1
				self.blocks.pop(index)


		for i in range (num_complete):
			self.blocks.insert(0, [0] * self.width)

		self.score += ((2 ** num_complete) - 1)

	def get_score(self):
		return self.score