# intro for fydo.net (yay for shameless plugs)

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

class Intro:
	def __init__(self):
		self.part1 = pygame.image.load(os.path.join('data', 'intro1.png')).convert()
		self.part2 = pygame.image.load(os.path.join('data', 'intro2.png')).convert()
		self.music = pygame.mixer.Sound(os.path.join('data', 'intro.ogg'))

	def DisplayIntro(self, screen, noSound):
		
		if (not noSound):
			self.music.play()
		pygame.time.wait(200)
		
		#fade in 1
		for x in range(40):
			screen.fill((0,0,0))
			work = self.part1
			#self.work.blit(part1, (0,0))
			work.set_alpha((x * 255) / 40.0, RLEACCEL)
			screen.blit(work, (0,0))
			pygame.display.flip()
			pygame.time.wait(10)
			
		
		#hold
		screen.blit(self.part1, (0,0))
		pygame.display.flip()
		pygame.time.wait(100) #tweak me.. oh yeah
		
		#fade in 2
		for x in range(30):
			work = self.part2
			screen.blit(self.part1, (0,0))
			work.set_alpha((x * 255) / 30.0, RLEACCEL)
			screen.blit(work, (0,0))
			pygame.display.flip()
			pygame.time.wait(10)
			
		#hold
		screen.blit(self.part2, (0,0))
		pygame.display.flip()
		pygame.time.wait(1000)
		
		#fade out
		for x in range(50):
			temp = x
			x = 50 - x
			screen.fill((0,0,0))
			work = self.part2
			work.set_alpha((x * 255) / 50.0, RLEACCEL)
			screen.blit(work, (0,0))
			pygame.display.flip()
			pygame.time.wait(10)
			
		screen.fill((0,0,0))
		pygame.display.flip()
		pygame.time.wait(500)
			
		
	
		
		
		
	