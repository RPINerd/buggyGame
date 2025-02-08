"""The potatoes for the game (meat is coming soon, hopefully) ;)"""

import sys
from pathlib import Path

import pygame
from pygame.locals import K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP, KEYDOWN, KEYUP, RLEACCEL, K_d

WhiteHit = (255, 255, 255, 255)
BlackHit = (0, 0, 0, 255)
LogicalFPS = 64.0
ticks_per_frame = (1000.0 / LogicalFPS)
MaxFrameSkip = 2

ROOT = Path(__file__).parent.parent


class Player:

    """"""

    def __init__(self) -> None:
        """"""
        self.rect = (50, 200)  # defaults
        self.xvec = 0.000
        self.yvec = 0.000
        self.xaccel = 0.000
        self.yaccel = 100.000
        self.xacceltimer = 0.00
        self.yacceltimer = 0.00
        self.oldrect = (0, 0)
        self.image = pygame.image.load("data/buggy.png").convert_alpha()
        self.baseImage = self.image
        self.moveLeft = False
        self.moveRight = False
        # self.dir = 0 #rotation amt
        self.falling = True
        self.dmove = 0.00
        self.curFrame = 0


class Game:

    """"""

    def __init__(self, joy: bool, mute_audio: bool) -> None:
        """"""
        self.player = Player()
        self.level = 1
        self.imglevel = pygame.image.load(Path.joinpath(ROOT, "data", "level1.png")).convert()
        self.imghitmask = pygame.image.load(Path.joinpath(ROOT, "data", "level1-hitmask.png")).convert()
        self.music = pygame.mixer.Sound(Path.joinpath(ROOT, "data", "game-audio1.ogg"))
        self.screenxloc = 0
        self.thetime = 0.0000  # pygame.time.get_ticks()
        self.timerdiff = 0
        self.secsperframe = 0
        self.useJoystick = joy
        self.mute_audio = mute_audio
        self.Debug = False
        self.lives = 3
        self.thefont = pygame.font.Font(Path.joinpath(ROOT, "data", "Vera.ttf"), 10)

    def LoadLevel(self, loadimage: bool) -> None:
        if loadimage:
            self.imglevel = pygame.image.load(Path.joinpath(ROOT, "data", f"level{self.level}.png")).convert()
            self.imghitmask = pygame.image.load(Path.joinpath(ROOT, "data", f"level{self.level}-hitmask.png")).convert()
        self.screenxloc = 0
        self.player.__init__()

    def ComputeMovement(self, timePassed, screen):
        # v = v + a * dt
        # x = x + v * dt

        # print("start compute'

        if ((self.player.moveLeft) and (self.player.xaccel > -40.0)):
            self.player.xaccel -= 10

        if ((self.player.moveRight) and (self.player.xaccel < 40.0)):
            self.player.xaccel += 10

        if (self.player.falling):
            # self.player.yaccel += 9.8 #acceleration due to gravity on earth
            self.player.yaccel += 6  # acceleration due to gravity on moon is really 1.6, but thats too low for me

        # print("xaccel is %f' % self.player.xaccel
        # print("yaccel is %f' % self.player.yaccel

        if ((not self.player.moveRight) and (not self.player.moveLeft) and (not self.player.falling)):
            self.player.xvec /= 1.03  # slow down!
            if (self.player.xvec < 1) and (self.player.xvec > -1):
                self.player.xvec = 0

        # timePassed = (timePassed / 1000.000) #convert to seconds

        self.player.xvec = (self.player.xvec + (self.player.xaccel * timePassed))
        self.player.yvec = (self.player.yvec + (self.player.yaccel * timePassed))
        self.player.yvec = min(self.player.yvec, 200)

        self.player.dmove = self.player.dmove + (self.player.xvec * timePassed)

        if (self.player.dmove > 5) or (self.player.dmove < -5):
            self.player.curFrame += 1
            self.player.dmove = 0
            if self.player.curFrame > 5:
                self.player.curFrame = 0

        # print("xvec is %f' % self.player.xvec
        # print("yvec is %f' % self.player.yvec

        self.player.rect = (self.player.rect[0] + (self.player.xvec * timePassed), self.player.rect[1])
        self.player.rect = (self.player.rect[0], self.player.rect[1] + (self.player.yvec * timePassed))

        # move the screen if needed
        if ((self.player.rect[0] > 288) and (self.screenxloc < 2540)):
            self.player.rect = (self.player.rect[0] - (self.player.xvec * timePassed), (self.player.rect[1]))
            self.screenxloc += (self.player.xvec * timePassed)
        # handle boundarys
        if (self.player.rect[0] < 2):
            self.player.rect = (2, self.player.rect[1])
        if (self.player.rect[0] > 550):
            # print("Go to next level! Yeah!'
            # self.music.stop
            self.winlevel(screen)
            # self.fadein(screen)
            self.level += 1
            if self.level > 3:
                return False
            self.LoadLevel(True)
        if (self.player.rect[1] > 480):  # fell into a hole
            self.die(screen)
            if (self.lives > 0):
                self.lives -= 1
                self.LoadLevel(False)
                return True
            return False

        return True

    def JumpButton(self):
        if not self.player.falling:
            self.player.falling = True
            self.player.yvec = -250.0
            self.player.rect = ((self.player.rect[0], self.player.rect[1] - 2))

    def GetAt(self, x, y):
        if (y > 479) or (y < 0):
            return WhiteHit

        return self.imghitmask.get_at((int(x), int(y)))

    def winlevel(self, screen):

        # screen.blit(self.imglevel, (0, 0), (self.screenxloc, 0, 640, 480))
        # screen.blit(self.player.image, (self.player.rect[0] + 3, self.player.rect[1]), ((6 * 64), 0, 64, 64))
        # pygame.display.flip()
        winimage = pygame.image.load(Path.joinpath(ROOT, "data", "winlevel.png")).convert_alpha()

        backup = self.imglevel

        backup.blit(screen, (0, 0))
        for x in range(180):
            screen.blit(backup, (0, 0))
            pos = winimage.get_rect(centerx=screen.get_width() / 2, centery=x)
            screen.blit(winimage, (pos))
            pygame.display.flip()
            pygame.time.wait(5)

        pygame.time.wait(300)
        backup.blit(screen, (0, 0))
        for x in range(50):
            x = 50 - x
            screen.fill((0, 0, 0))
            work = backup
            work.set_alpha((x * 255) / 50.0, RLEACCEL)
            screen.blit(work, (0, 0))
            pygame.display.flip()
            pygame.time.wait(10)

        # self.music.fadeout(2000)
        pygame.time.wait(100)
        self.thetime = pygame.time.get_ticks()

    def die(self, screen):

        if self.lives == 0:
            self.music.fadeout(2000)
        screen.blit(self.imglevel, (0, 0), (self.screenxloc, 0, 640, 480))
        screen.blit(self.player.image, (self.player.rect[0] + 3, self.player.rect[1]), ((6 * 64), 0, 64, 64))
        self.drawStatus(screen, "You have broken the buggy! Oh noes!")
        pygame.display.flip()
        loseimage = pygame.image.load(Path.joinpath(ROOT, "data", "lose.png")).convert_alpha()

        backup = pygame.Surface((640, 480))

        backup.blit(screen, (0, 0))
        for x in range(180):
            screen.blit(backup, (0, 0))
            pos = loseimage.get_rect(centerx=screen.get_width() / 2, centery=x)
            screen.blit(loseimage, (pos))
            pygame.display.flip()
            pygame.time.wait(5)

        pygame.time.wait(600)
        backup.blit(screen, (0, 0))
        for x in range(50):
            x = 50 - x
            screen.fill((0, 0, 0))
            work = backup
            work.set_alpha((x * 255) / 50.0, RLEACCEL)
            screen.blit(work, (0, 0))
            pygame.display.flip()
            pygame.time.wait(15)

        screen.fill((0, 0, 0))
        self.imglevel.set_alpha(255)
        pygame.time.wait(100)
        self.thetime = pygame.time.get_ticks()

    def DoInputStuff(self):
        # input!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT):
                    self.player.moveLeft = True
                elif (event.key == K_RIGHT):
                    self.player.moveRight = True
                elif (event.key == K_ESCAPE):
                    self.music.fadeout(500)
                    return False
                elif event.key in {K_SPACE, K_UP}:
                    self.JumpButton()
                elif (event.key == K_d):
                    self.Debug = not self.Debug

            elif event.type == KEYUP:
                if (event.key == K_LEFT):
                    self.player.moveLeft = False
                elif (event.key == K_RIGHT):
                    self.player.moveRight = False

        if self.useJoystick:
            for x in range(self.numbuttons):
                if self.Joystick.get_button(x):
                    self.JumpButton()
            if self.Joystick.get_axis(0) >= 0.5:
                self.player.moveRight = True
                self.player.moveLeft = False
            elif self.Joystick.get_axis(0) <= -0.5:
                self.player.moveLeft = True
                self.player.moveRight = False
            else:
                self.player.moveLeft = False
                self.player.moveRight = False

        return True

    def CheckIntersections(self, screen):
            # right below left wheel
        pixelcheck1 = self.GetAt((self.screenxloc + self.player.rect[0]), self.player.rect[1] + 65)
            # right below right wheel
        pixelcheck2 = self.GetAt((self.screenxloc + self.player.rect[0] + 64), (self.player.rect[1] + 65))
            # immediately to the left of the buggy (5px up from bottom)
        pixelcheck3 = self.GetAt((self.screenxloc + self.player.rect[0]), (self.player.rect[1] + 59))
            # to the right
        pixelcheck4 = self.GetAt((self.screenxloc + self.player.rect[0] + 64), (self.player.rect[1] + 59))

            # 5 and 6 are to check underneath the buggy (in case there are rocks, you know)
        pixelcheck5 = self.GetAt((self.screenxloc + self.player.rect[0] + 22), self.player.rect[1] + 65)
        pixelcheck6 = self.GetAt((self.screenxloc + self.player.rect[0] + 44), self.player.rect[1] + 65)
            # if theres a pixel under the car, you can ramp up!
        moveupcheck1 = self.GetAt((self.screenxloc + self.player.rect[0] + 64), (self.player.rect[1] + 60))
        moveupcheck2 = self.GetAt((self.screenxloc + self.player.rect[0] + 64), (self.player.rect[1] + 61))
        moveupcheck3 = self.GetAt((self.screenxloc + self.player.rect[0] + 64), (self.player.rect[1] + 62))
        moveupcheck4 = self.GetAt((self.screenxloc + self.player.rect[0] + 64), (self.player.rect[1] + 63))
            # these ones are for the back end (just in case, you know!)
        moveupcheck5 = self.GetAt((self.screenxloc + self.player.rect[0]), (self.player.rect[1] + 60))
        moveupcheck6 = self.GetAt((self.screenxloc + self.player.rect[0]), (self.player.rect[1] + 61))
        moveupcheck7 = self.GetAt((self.screenxloc + self.player.rect[0]), (self.player.rect[1] + 62))
        moveupcheck8 = self.GetAt((self.screenxloc + self.player.rect[0]), (self.player.rect[1] + 63))

        # print("pixelchecks:'
            # print("at %d %d :' % (self.player.rect[0], (self.player.rect[1] + 65))
            # print(pixelcheck1
            # print(pixelcheck2

        if (pixelcheck1 == WhiteHit) and (pixelcheck2 == WhiteHit):
            self.player.falling = True
        elif self.player.yaccel > 0:
            self.player.falling = False
            self.player.yaccel = 0
            self.player.yvec = 0

        if (pixelcheck5 == BlackHit) and (pixelcheck6 == BlackHit):
            if self.player.yaccel > 0:
                self.player.falling = False
                self.player.yaccel = 0
                self.player.yvec = 0

        if ((pixelcheck3 == BlackHit) or (pixelcheck4 == BlackHit)) and (self.player.xaccel != 0):
            self.die(screen)
            if (self.lives > 0):
                self.lives -= 1
                self.LoadLevel(False)
                return True
            return False

        if (moveupcheck1 == BlackHit) or (moveupcheck5 == BlackHit):
            self.player.rect = ((self.player.rect[0], self.player.rect[1] - 4))
        elif (moveupcheck2 == BlackHit) or (moveupcheck6 == BlackHit):
            self.player.rect = ((self.player.rect[0], self.player.rect[1] - 3))
        elif (moveupcheck3 == BlackHit) or (moveupcheck7 == BlackHit):
            self.player.rect = ((self.player.rect[0], self.player.rect[1] - 2))
        elif (moveupcheck4 == BlackHit) or (moveupcheck8 == BlackHit):
            self.player.rect = ((self.player.rect[0], self.player.rect[1] - 1))

        return True

    def drawStatus(self, screen, statustext):

        statusBar = pygame.Surface((640, 12)).convert()
        statusBar.fill((20, 20, 20))
        screen.blit(statusBar, (0, 468))

        text = self.thefont.render(statustext, 1, (255, 255, 255))
        textpos = text.get_rect(centerx=screen.get_width() / 2, centery=(468 + (text.get_height() / 2)))
        screen.blit(text, textpos)

    def Go(self, screen):
        # init stuff
        if (pygame.joystick.get_count() > 0) and (self.useJoystick == True):
            self.Joystick = pygame.joystick.Joystick(0)
            self.Joystick.init()
            self.numbuttons = self.Joystick.get_numbuttons()
            # print("Found joystick! Using %s' % self.Joystick.get_name()

        # DoInputStuff()

        # init timer things
        last_ticks = 0
        tick_elapsed = 0

        # play music
        if (not self.mute_audio):
            self.music.play()

        while 1:
            self.thetime = pygame.time.get_ticks()
            tick_elapsed += self.thetime - last_ticks
            last_ticks = self.thetime

            if (tick_elapsed > (ticks_per_frame * 4)):
                tick_elapsed = 0

            frames = 0

            if (tick_elapsed > ticks_per_frame):
                while ((tick_elapsed > ticks_per_frame) and (frames < MaxFrameSkip)):
                    tick_elapsed -= ticks_per_frame
                    timestep = 1.0 / LogicalFPS

                    # everyone loves input
                    if not self.DoInputStuff():
                        return

                    # compute movements
                    if not self.ComputeMovement(timestep, screen):
                        return

                    # check for intersects
                    if not self.CheckIntersections(screen):
                        return

                    frames += 1

            # draw everyone!
            if (self.Debug):
                screen.blit(self.imghitmask, (0, 0), (self.screenxloc, 0, 640, 480))
            else:
                screen.blit(self.imglevel, (0, 0), (self.screenxloc, 0, 640, 480))

            screen.blit(self.player.image, (self.player.rect), ((self.player.curFrame * 64), 0, 64, 64))

            self.drawStatus(screen, "Level: %d     Lifes: %d" % (self.level, self.lives))

            if self.timerdiff == 0:
                timer = pygame.time.get_ticks()
            # self.timerdiff = ((pygame.time.get_ticks() - self.thetime) / 1000.000)#convert to seconds
            pygame.display.flip()
            # delay time
            pygame.time.wait(5)
