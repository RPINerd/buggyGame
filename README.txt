buggyGame
=========

Originally an Entry in Ludum Dare 8.5 (warmup) (http://www.ludumdare.com)
by Chris 'fydo' Hopp - http://www.fydo.net


STORYLINE:

You're an astronaut that is about to go the moon on a mission, 
 but your moon buggy's navigational computer has bluescreened!
You must manually guide the buggy to the launchpad and touch 
 the rocket to get to the moon, then explore the surface of the moon.
Also keep in mind that your moon buggy is very fragile, so
 don't run into anything!


DEPENDENCIES:

You might need to install some of these before running the game:

  Python:     http://www.python.org/
  PyGame:     http://www.pygame.org/


RUNNING THE GAME:

On Windows or Mac OS X, locate the "buggyGame.py" file and double-click it.

Otherwise open a terminal / console and "cd" to the game directory and run:

  python buggyGame.py
  
Optional commandline arguments
  '-f' or '--fullscreen'    -    enable fullscreen mode
  '-j' or '--joystick'      -    enable joystick (note that this disables use of the keyboard)
  '-n' or '--nosound'       -    disable sound
  '-s' or '--skipintro'     -    skip the 'fydo.net' credit intro
  

HOW TO PLAY THE GAME:

The main menu consists of a green checkmark and a red 'X'
Use keyboard arrows to choose your selection and spacebar or return
to confirm your selection. The checkmark begins the game, and the 'X' 
will exit.

There are a total of 3 levels.


CONTROLS:

    Keyboard:
    Left and Right arrows    -    Accelerate left/right
    Up arrow or Spacebar     -    Jump
    'D' Key                  -    Enable Debug Mode

    Joystick:
    Axis #1 left/right       -    Accelerate left/right
    Any button at all        -    Jump


LICENSE:

The code is licensed under the GPL, as noted below. 
The assets (everything in the data directory) is under the Free Art License.
Please see LICENSE.txt in the data directory for more information. Thanks!


buggyGame - an exploration/survival game (Code only)
Copyright (C) 2007  Chris Hopp

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

