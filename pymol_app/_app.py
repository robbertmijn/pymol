#!/usr/bin/env python

import pygame
import csv
import argparse
from pymol_app._molfuncs import *

def app():

	parser = argparse.ArgumentParser()
	parser.add_argument("file", default=None, nargs="?", help="The path to the dragged file")
	args = parser.parse_args()

	# load csv with list of players and the color of their screen
	if args.file:
		with open(args.file, 'r') as f:
			reader = csv.reader(f)
			kandidaten = dict(reader)
	else:
		# if no file is provided, use some default names for demo
		kandidaten = {'speler1':'green', 'speler2':'green', 'speler3':'red'}

	# start pygame, initialize the clock, screen, and a font
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode([600, 500], pygame.FULLSCREEN)
	base_font = pygame.font.SysFont('Helvetica', 64)
	
	# start with empty text, set state to being ready for input
	user_text = ''
	state = 'input'

	# start polling for response and keep flipping screen
	while 1:

		state, user_text  = check_input(state, user_text, kandidaten)

		if state == 'input':
			text_surface = base_font.render(user_text, True, "white")
			bg_col = 'black'
			screen.fill(bg_col)
			screen.blit(text_surface, (screen.get_width()/2, screen.get_height()/2))

		if state == 'suspense':
			pulse_screen(screen, clock)
			state = 'reveal'

		if state == 'reveal':
			bg_col = kandidaten[user_text]
			screen.fill(bg_col)

		pygame.display.flip()
		clock.tick(60)