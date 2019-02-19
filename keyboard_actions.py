import board
import sys
import select

DROP_SHAPE = 'drop_shape'
MOVE_RIGHT = 'move_right'
MOVE_LEFT = 'move_left'
MOVE_DOWN = 'move_down'
ROTATE_RIGHT = 'rotate_right'
ROTATE_LEFT = 'rotate_left'
SWAP = 'swap'
NO_INPUT = 'no_input'
KILL_ME = 'kill_me'

def get_raw_unblocking_keyboard_input():
	import sys, tty, termios
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	tty.setraw(sys.stdin.fileno())

	i,o,e = select.select([sys.stdin],[],[],1)
	for s in i:
		if s == sys.stdin:
			input = sys.stdin.read(1)
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
			return input
	termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return False


def get_next_action():
	key = get_raw_unblocking_keyboard_input()
	if key == 'w':
		return DROP_SHAPE
	if key == 'd':
		return MOVE_RIGHT
	if key == 'a':
		return MOVE_LEFT
	if key == 's':
		return MOVE_DOWN
	if key == 'j':
		return ROTATE_LEFT
	if key == 'k':
		return ROTATE_RIGHT
	if key == 'q' or key == 'l':
		return SWAP
	if key == '9':
		return KILL_ME
	return NO_INPUT


