"""Menu for the game"""

import sys

import pygame
from pygame.locals import K_ESCAPE, K_LEFT, K_RETURN, K_RIGHT, K_SPACE, RLEACCEL


class Menu:

    """Menu for the game"""

    def __init__(self, joystick: bool) -> None:
        """"""
        self.bgimage: pygame.Surface = pygame.image.load("data/menubg.png").convert()
        self.selectimage: pygame.Surface = pygame.image.load("data/select.png").convert_alpha()
        self.selectYes: bool = True
        self.useJoystick: bool = joystick
        if pygame.joystick.get_count() > 0 and self.useJoystick:
            self.Joystick = pygame.joystick.Joystick(0)
            self.Joystick.init()
            self.numbuttons = self.Joystick.get_numbuttons()

    def select(self, screen: pygame.Surface) -> bool:
        """"""
        # FANCY FADE OUT!
        for x in range(50):
            temp = x
            x = 50 - x
            screen.fill((0, 0, 0))
            work = self.bgimage
            work.set_alpha((x * 255) / 50.0, RLEACCEL)
            screen.blit(work, (0, 0))
            pygame.display.flip()
            pygame.time.wait(10)
        return self.selectYes

    def render(self, screen: pygame.Surface) -> bool:
        """"""
        pygame.mixer.stop

        # FANCY FADE IN OMG
        for x in range(40):
            screen.fill((0, 0, 0))
            work = self.bgimage
            work.set_alpha((x * 255) / 40.0, RLEACCEL)
            screen.blit(work, (0, 0))
            pygame.display.flip()
            pygame.time.wait(10)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type != pygame.KEYDOWN:
                    continue

                if event.key in {K_RIGHT, K_LEFT}:
                    self.selectYes = not self.selectYes
                elif event.key in {K_SPACE, K_RETURN}:
                    return self.select(screen)
                elif event.key == K_ESCAPE:
                    self.selectYes = False
                    return self.select(screen)

            if self.useJoystick:
                for x in range(self.numbuttons):
                    if self.Joystick.get_button(x):
                        return self.select(screen)
                if (self.Joystick.get_axis(0) >= 0.5):
                    self.selectYes = False
                elif (self.Joystick.get_axis(0) <= -0.5):
                    self.selectYes = True

            screen.blit(self.bgimage, (0, 0))
            selectloc = (0, 0)
            if self.selectYes:
                selectloc = (89, 38)
            else:
                selectloc = (349, 42)

            screen.blit(self.selectimage, selectloc)
            pygame.display.flip()
            pygame.time.wait(25)
