"""
    buggyGame - an exploration/survival game

    Entry for LD Warmup
    All code and assets created by Chris Hopp (http://www.fydo.net)

    Update to python 3 by RPINerd
"""


import pygame
from pygame.locals import FULLSCREEN

from .intro import Intro
from .menu import Menu
from .potatoes import Game

SYSVERSION = "1.0"


def main(fullscreen: bool, joystick: bool, nosound: bool, skipfydo: bool) -> None:
    """
    Main entry point for the game.

    Args:
        fullscreen (bool): Enable fullscreen mode
        joystick (bool): Enable joystick use
        nosound (bool): Disable sound
        skipfydo (bool): Skip the fydo.net intro

    Returns:
        None
    """
    pygame.mixer.pre_init(22050, -16, 1, 2048)
    pygame.init()

    size = 640, 480
    if fullscreen:
        screen = pygame.display.set_mode(size, FULLSCREEN)
        pygame.time.wait(1000)  # wait for the computer to switch video modes
    else:
        screen = pygame.display.set_mode(size)  # , HWSURFACE|DOUBLEBUF)

    pygame.mouse.set_visible(0)

    pygame.display.set_caption(f"fydo\'s buggyGame v{SYSVERSION}")

    # intro time!
    if not skipfydo:
        the_intro = Intro()
        the_intro.render(screen, nosound)

    while True:
        screen.fill((0, 0, 0))  # ~ "No lights ..."
        pygame.mixer.stop  # ~ "No music ..."

        # Purge input queue
        pygame.event.get()

        # Do introscreen stuff  here
        the_menu = Menu(joystick)

        if not the_menu.render(screen):
            pygame.display.quit()
            return

        the_game = Game(joystick, nosound)
        the_game.Go(screen)
