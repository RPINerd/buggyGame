# buggyGame

A simple game where you drive a moon buggy on a mission to the moon!

## Credits

This was originally a warmup entry in [Ludum Dare](http://www.ludumdare.com) 8.5 by Chris 'fydo' Hopp (http://www.fydo.net)

## Story

You're an astronaut that is about to go the moon on a mission, but your moon buggy's navigational computer has bluescreened!
You must manually guide the buggy to the launchpad and touch the rocket to get to the moon, then explore the surface of the moon.
Also keep in mind that your moon buggy is very fragile, so don't run into anything!

## Dependencies

[Python](http://www.python.org/) - Updated with 3.13, but will likely work with 3.9-3.12
[PyGame](http://www.pygame.org/) - Updated with 2.6.1, possible to be compatible with older versions

## Launching the Game

### Windows/Mac OS

Locate the "play.py" file and double-click it. (No idea if this is still how it works, but it's worth a shot)

### Linux

```bash
git clone https://github.com/RPINerd/buggyGame.git
cd buggyGame
python play.py
```

### Command Line Arguments

  `-f`/`--fullscreen`: enable fullscreen mode
  `-j`/`--joystick`  : enable joystick (note that this disables use of the keyboard)
  `-n`/`--nosound`   : disable sound
  `-s`/`--skipintro` : skip the 'fydo.net' credit intro

## Playing

The main menu consists of a green checkmark and a red 'X'
Use keyboard arrows to choose your selection and spacebar or return to confirm your selection.
The checkmark begins the game, and the 'X' will exit.

There are a total of 3 levels.

### Controls

#### Keyboard

- Left and Right arrows - Accelerate left/right
- Up arrow or Spacebar  - Jump
- 'D' Key               - Enable Debug Mode

#### Joystick

- Axis #1 left/right - Accelerate left/right
- Any button at all  - Jump
