"""Intro for fydo.net (yay for shameless plugs)"""


import pygame
from pygame.locals import RLEACCEL


class Intro:

    """"""

    def __init__(self) -> None:
        """"""
        self.part1 = pygame.image.load("data/intro1.png").convert()
        self.part2 = pygame.image.load("data/intro2.png").convert()
        self.music = pygame.mixer.Sound("data/intro.ogg")

    def render(self, screen: pygame.Surface, mute_sound: bool) -> None:
        """"""
        if not mute_sound:
            self.music.play()
        pygame.time.wait(200)

        # Fade in 1
        for x in range(40):
            screen.fill((0, 0, 0))
            work = self.part1
            # self.work.blit(part1, (0,0))
            work.set_alpha((x * 255) / 40.0, RLEACCEL)
            screen.blit(work, (0, 0))
            pygame.display.flip()
            pygame.time.wait(10)

        # Hold
        screen.blit(self.part1, (0, 0))
        pygame.display.flip()
        pygame.time.wait(100)  # tweak me.. oh yeah

        # Fade in 2
        for x in range(30):
            work = self.part2
            screen.blit(self.part1, (0, 0))
            work.set_alpha((x * 255) / 30.0, RLEACCEL)
            screen.blit(work, (0, 0))
            pygame.display.flip()
            pygame.time.wait(10)

        # Hold
        screen.blit(self.part2, (0, 0))
        pygame.display.flip()
        pygame.time.wait(1000)

        # Fade out
        for x in range(50):
            temp = x
            x = 50 - x
            screen.fill((0, 0, 0))
            work = self.part2
            work.set_alpha((x * 255) / 50.0, RLEACCEL)
            screen.blit(work, (0, 0))
            pygame.display.flip()
            pygame.time.wait(10)

        screen.fill((0, 0, 0))
        pygame.display.flip()
        pygame.time.wait(500)
