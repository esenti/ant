#!/usr/bin/env python

import pygame
import sys

pygame.init()

size = width, height = 640, 480
speed = [2, 2]
bg_color = 200, 200, 200

screen = pygame.display.set_mode(size)

anteater = pygame.transform.scale(pygame.image.load("anteater.png"), (110, 143))
anteaterrect = anteater.get_rect()


dir_x = dir_y = 0

hist = []

while 1:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				dir_x = 0
				dir_y = -1
			elif event.key == pygame.K_DOWN:
				dir_x = 0
				dir_y = 1
			elif event.key == pygame.K_LEFT:
				dir_x = -1
				dir_y = 0
			elif event.key == pygame.K_RIGHT:
				dir_x = 1
				dir_y = 0


	hist.append(anteaterrect)

	anteaterrect = anteaterrect.move((dir_x, dir_y))

	screen.fill(bg_color)

	if(len(hist) > 10):


		surface = pygame.Surface(anteater.get_size(), depth=24)
		key = (0,255,0)

		surface.fill(key, surface.get_rect())
		surface.set_colorkey(key)

		surface.blit(anteater, (0,0))
		surface.set_alpha(128)
		screen.blit(anteater, hist[0])
		hist.pop(0)


	#anteater.set_alpha(1.0)

	screen.blit(anteater, anteaterrect)
	pygame.display.flip()
