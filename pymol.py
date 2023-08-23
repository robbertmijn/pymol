#!/usr/bin/env python

kandidaten = {'rob':'green', 
	      'lyke':'green', 
		  'robbert':'red'}


# import sys module
import pygame
import sys
import math
import random

pygame.init()

clock = pygame.time.Clock()

# it will display on screen
screen = pygame.display.set_mode([600, 500])

# basic font for user typed
base_font = pygame.font.Font(None, 32)
user_text = ''

state = 'input'

def interpolate_color(color1, color2, t):
    return tuple(int(c1 + (c2 - c1) * t) for c1, c2 in zip(color1, color2))

def pulse_screen():

	start_time = pygame.time.get_ticks()

	# Colors
	color1 = (50, 50, 50)
	color2 = (200, 200, 200)

	# Number of frames for the transition
	freq = 1.0
	dur = random.uniform(2, 3)

	while 1:
		current_time = pygame.time.get_ticks()

		elapsed_time = (current_time - start_time) / 1000.0  # Convert to seconds

		if elapsed_time >= dur:
			break

		# Calculate the oscillation parameter between 0 and 1
		oscillation_parameter = 0.5 + 0.5 * math.sin(2 * math.pi * freq * elapsed_time)

		# Calculate the interpolated color based on the oscillation parameter
		current_color = interpolate_color(color1, color2, oscillation_parameter)

		# Fill the screen with the current color
		screen.fill(current_color)

		# Update the display
		pygame.display.flip()

		# Cap the frame rate
		clock.tick(60)

def main():

	while True:

		for event in pygame.event.get():

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_BACKSPACE:
					user_text = user_text[:-1]
					
				elif event.key == pygame.K_RETURN:
					
					if state == 'reveal':
						state = 'input'
						user_text = ''

					elif user_text in list(kandidaten.keys()):
						state = 'suspense'
					else:
						user_text = ''

				else:
					user_text += event.unicode

		if state == 'input':
			
			text_surface = base_font.render(user_text, True, "white")
			# it will set background color of screen
			bg_col = 'black'
			screen.fill(bg_col)
			# render at position stated in arguments
			screen.blit(text_surface, (screen.get_width()/2, screen.get_height()/2))

		if state == 'suspense':
			pulse_screen()
			state = 'reveal'

		if state == 'reveal':
			bg_col = kandidaten[user_text]
			screen.fill(bg_col)

		
		# display.flip() will update only a portion of the
		# screen to updated, not full area
		pygame.display.flip()
		
		# clock.tick(60) means that for every second at most
		# 60 frames should be passed.
		clock.tick(60)

if __name__ == "__main__":
    main()