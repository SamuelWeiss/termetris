from board import tetris_board
from keyboard_actions import *
from shape import shape, all_shapes

import time
import math
import sys, select
import random

def calculate_next_frame(level):
	now = time.time()
	return now + (1.0 / (level * 0.5 + 0.5))

# avoid weird screen flickering
def composite_display(board, score, level, falling_shape, holding_shape, next_shape):
	board_rows = board.render_board(falling_shape)
	next_shape_array = next_shape.get_pretty_shape_array()
	if holding_shape is not None:
		holding_shape_title = "The piece you're holding is:\n"
		holding_shape_array = holding_shape.get_pretty_shape_array()
	else:
		holding_shape_title = "You're not currently holding anything\n"
		holding_shape_array = ["    "] * 4
	single_string = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
	single_string += (board_rows[0] + "\n")
	single_string += (board_rows[1] + " Your current score is: " + str(score) + "\n")
	single_string += (board_rows[2] + " Your current level is: " + str(level) + "\n")
	single_string += (board_rows[3] + " Your next piece  is: \n")
	single_string += (board_rows[4] + " " + next_shape_array[0] + "\n")
	single_string += (board_rows[5] + " " + next_shape_array[1] + "\n")
	single_string += (board_rows[6] + " " + next_shape_array[2] + "\n")
	single_string += (board_rows[6] + " " + next_shape_array[3] + "\n")
	single_string += (board_rows[7] + " " + holding_shape_title)
	single_string += (board_rows[8] + " " + holding_shape_array[0] + "\n")
	single_string += (board_rows[9] + " " + holding_shape_array[1] + "\n")
	single_string += (board_rows[10] + " " + holding_shape_array[2] + "\n")
	single_string += (board_rows[11] + " " + holding_shape_array[3] + "\n")
	for i in xrange(12, len(board_rows), 1):
		single_string += (board_rows[i] + "\n")

	print single_string

def get_next_shape(shapes_to_fall):
	if len(shapes_to_fall) == 0:
		for shape in all_shapes:
			shapes_to_fall.append(shape)
		random.shuffle(shapes_to_fall)
	return shapes_to_fall


def run_tetris():

	board = tetris_board()
	level = 1
	lost = False
	holding_shape = None
	shapes_to_fall = get_next_shape([])
	falling_shape = shape(shapes_to_fall.pop(0))
	next_shape = shape(shapes_to_fall.pop(0))
	has_swapped = False
	last_action_time = 0

	while not lost:

		composite_display(board, board.score, level, falling_shape, holding_shape, next_shape)
		fall_time = calculate_next_frame(level)

		while time.time() < fall_time:
			# look for input
			action = get_next_action(fall_time - time.time())
			if action != NO_INPUT:
				last_action_time = time.time()

			if action == KILL_ME:
				exit(0)
			elif action ==  ROTATE_RIGHT:
				falling_shape = board.rotate_shape_right(falling_shape)
			elif action == ROTATE_LEFT:
				falling_shape = board.rotate_shape_left(falling_shape)
			elif action == MOVE_RIGHT:
				falling_shape = board.move_shape_right(falling_shape)
			elif action == MOVE_LEFT:
				falling_shape = board.move_shape_left(falling_shape)
			elif action == DROP_SHAPE:
				falling_shape = board.drop_shape(falling_shape)
			elif action == MOVE_DOWN:
				falling_shape = board.fall_shape(falling_shape, True)
			elif action == SWAP:
				if holding_shape is None:
					holding_shape = falling_shape
					holding_shape.reset_position()
					shapes_to_fall = get_next_shape(shapes_to_fall)
					falling_shape = shape(shapes_to_fall.pop(0))
					has_swapped = True
				if holding_shape is not None and not has_swapped:
					has_swapped = True
					tmp = falling_shape
					falling_shape = holding_shape
					holding_shape = tmp
					holding_shape.reset_position()

			if falling_shape is None:
				falling_shape = next_shape
				shapes_to_fall = get_next_shape(shapes_to_fall)
				next_shape = shape(shapes_to_fall.pop(0))
				has_swapped = False

			composite_display(board, board.score, level, falling_shape, holding_shape, next_shape)

			if board.score / 25 > level:
				level += 1

		falling_shape = board.fall_shape(falling_shape, not (time.time() - last_action_time) > 1)
		if falling_shape is None:
			falling_shape = next_shape
			shapes_to_fall = get_next_shape(shapes_to_fall)
			next_shape = shape(shapes_to_fall.pop(0))
			has_swapped = False
			if board.has_intersection(falling_shape):
				lost = True

def print_help_message():
	help_message = """
Welcome to termetris! It's tetris in the terminal.
The controls are as follows:
w   -> this drops the current falling piece into the board
	   (As a helpful tool its position is highlighted with stars)
a   -> move the current falling piece left
d   -> move the current falling piece left
s   -> drop the current falling piece down once
j/k -> rotate the falling piece
q/l -> swap the falling piece for the held piece
9   -> exit termetris
	"""
	print help_message

def main():
	if len(sys.argv) >= 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help" or sys.argv[1] == "help"):
		print_help_message()
		print "Got that? (y/n)"
		player_ready = raw_input()
		if player_ready.upper() != "Y":
			exit(0)
	run_tetris()



if __name__ == '__main__':
	main()