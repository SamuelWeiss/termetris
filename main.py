from board import tetris_board
import time
import math
from keyboard_actions import *
from shape import shape

import sys, select


def calculate_next_frame(level):
	now = time.time()
	return now + (1.0/(2 * level - 1))

def main():

	board = tetris_board()
	level = 1
	lost = False
	score = 0
	holding_shape = None
	falling_shape = shape()
	next_shape = shape()
	has_swapped = False

	# TODO: implement losing the game
	while not lost:

		blank_screen()
		draw_header(holding_shape, next_shape, board.get_score(), level)
		board.render_board(falling_shape)
		fall_time = calculate_next_frame(level)

		while time.time() < fall_time:
			# look for input
			action = get_next_action()

			# do the game logic
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
				falling_shape = board.fall_shape(falling_shape)
			elif action == SWAP:
				if holding_shape is None:
					holding_shape = falling_shape
					holding_shape.reset_position()
					falling_shape = shape()
					has_swapped = True
				if holding_shape is not None and not has_swapped:
					has_swapped = True
					tmp = falling_shape
					falling_shape = holding_shape
					holding_shape = tmp
					holding_shape.reset_position()

			if falling_shape is None:
				falling_shape = next_shape
				next_shape = shape()
				has_swapped = False

			blank_screen()
			draw_header(holding_shape, next_shape, board.get_score(), level)
			board.render_board(falling_shape)
			if board.score / 10 > level:
				level += 1
		falling_shape = board.fall_shape(falling_shape)
		if falling_shape is None:
			falling_shape = next_shape
			next_shape = shape()
			has_swapped = False

def draw_header(holding_shape, next_shape, score, level):
	print "Your current score is: " + str(score)
	print "the current level is: " + str(level)
	if holding_shape is not None:
		print "The piece you're holding is:"
		print holding_shape.get_pretty_shape()
	print "The next piece is:"
	print next_shape.get_pretty_shape()

def blank_screen():
	for i in range(10):
		print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"


if __name__ == '__main__':
	main()