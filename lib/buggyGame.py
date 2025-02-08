#!/usr/bin/python

# Entry for LD Warmup
# All code and assets created by Chris Hopp
# http://www.fydo.net

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

import pygame, os, sys, optparse
from pygame.locals import *
from intro import *
from menu import *
from potatoes import *

USAGE = """%prog [-fjns]"""
systemVersion = "0.3"
VERSION = "%prog v" + systemVersion

#run from the proper location
#os.chdir( os.path.dirname( sys.argv[0] ) )

def parse_options():
	"""parse_options() -> opts, args

	Parse any command-line options given.
	Returns both the parsed options and arguments.
	"""

	parser = optparse.OptionParser(usage=USAGE, version=VERSION)

	parser.add_option("-f", "--fullscreen",
		action="store_true", default=False, dest="fullscreen",
		help="enable fullscreen mode")

	parser.add_option("-j", "--joystick",
		action="store_true", default=False, dest="joystick",
		help="enable joystick use (disables keyboard)")
	
	parser.add_option("-n", "--nosound",
		action="store_true", default=False, dest="nosound",
		help="disable sound")
			
	parser.add_option("-s", "--skipintro",
		action="store_true", default=False, dest="skipintro",
		help="skip fydo.net intro")
	
	opts, args = parser.parse_args()
	return opts, args

def main(fullscreen, joystick, nosound, skipfydo):
	 # This game is so complex that we will attempt to enable psyco for a performance boost. (sarcasm)
        try:
                import psyco
                psyco.background()
                print 'psyco found and enabled!'
        except ImportError:
                print 'psyco not found! don\'t worry, this game doesn\'t really need it.'

	pygame.mixer.pre_init(22050, -16, 1, 2048)
	pygame.init()
	
	size = width, height = 640, 480
	if fullscreen:
		screen = pygame.display.set_mode(size, FULLSCREEN)
		pygame.time.wait(1000)#wait for the computer to switch video modes
	else:
		screen = pygame.display.set_mode(size) #, HWSURFACE|DOUBLEBUF)
	
	pygame.mouse.set_visible(0)
	
	pygame.display.set_caption('fydo\'s buggyGame v' + systemVersion )

	#intro time!
	if not skipfydo:
		theIntro = Intro()
		theIntro.DisplayIntro(screen, nosound)
	
	while 1:
		screen.fill( (0, 0, 0)) # ~ "No lights ..."
		pygame.mixer.stop # ~ "No music ..."
		
		# Purge input queue
		pygame.event.get()
		
		# Do introscreen stuff  here
		themenu = Menu(joystick)

		if not themenu.ShowMenu(screen):
			pygame.display.quit()
			return
		
		thegame = Game(joystick, nosound)
		thegame.Go(screen)
		

def starthere():
#if __name__ == '__main__':
	# Welcome the player
	print 'fydo\'s buggyGame v' + systemVersion + ' - http://www.fydo.net'

	#Parse the options up! Woo
	opts, args = parse_options()

	# Play time
	main(opts.fullscreen, opts.joystick, opts.nosound, opts.skipintro)
	
	# Say goodbye like every good little program should
	print '\nthanks for playing!'

if __name__ == '__main__':
	starthere()
