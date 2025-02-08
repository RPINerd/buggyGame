# menu for the game

#-------------------------------------------
#
# buggyGame - an exploration/survival game (Code only)
#Copyright (C) 2007  Chris Hopp
#
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#-------------------------------------------

import os, sys
import pygame
from pygame.locals import *

class Menu:
	def __init__(self, joystick):
		#load stuff
		self.bgimage = pygame.image.load(os.path.join('data', 'menubg.png')).convert()
		self.selectimage = pygame.image.load(os.path.join('data', 'select.png')).convert_alpha()
		self.selectYes = True
		self.useJoystick = joystick
		if (pygame.joystick.get_count() > 0) and (self.useJoystick == True):
			self.Joystick = pygame.joystick.Joystick(0)
			self.Joystick.init()
			self.numbuttons = self.Joystick.get_numbuttons()
	
	def PickIt(self, screen):
		#FANCY FADE OUT!
		for x in range(50):
			temp = x
			x = 50 - x
			screen.fill((0,0,0))
			work = self.bgimage
			work.set_alpha((x * 255) / 50.0, RLEACCEL)
			screen.blit(work, (0,0))
			pygame.display.flip()
			pygame.time.wait(10)
			return self.selectYes
			
	def ShowMenu(self, screen):
		#screen.fill((0,0,0))
		pygame.mixer.stop
		#FANCY FADE IN OMG
		for x in range(40):
			screen.fill((0,0,0))
			work = self.bgimage
			work.set_alpha((x * 255) / 40.0, RLEACCEL)
			screen.blit(work, (0,0))
			pygame.display.flip()
			pygame.time.wait(10)
		
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()
				elif event.type == KEYDOWN:
					if ((event.key == K_RIGHT) or (event.key == K_LEFT)):
						self.selectYes = not self.selectYes
					elif ((event.key == K_SPACE) or (event.key == K_RETURN)):
						return self.PickIt(screen)
					elif (event.key == K_ESCAPE):
						self.selectYes = False
						return self.PickIt(screen)
			
			if self.useJoystick:
				for x in range(self.numbuttons):
					if self.Joystick.get_button(x):
						return self.PickIt(screen)
				if (self.Joystick.get_axis(0) >= 0.5):
					self.selectYes = False
				elif (self.Joystick.get_axis(0) <= -0.5):
					self.selectYes = True
			
			screen.blit(self.bgimage, (0,0))
			selectloc = (0,0)
			if self.selectYes:
				selectloc = (89, 38)
			else:
				selectloc = (349, 42)
			
			screen.blit(self.selectimage, selectloc)
			pygame.display.flip()
			pygame.time.wait(25) #
					
		