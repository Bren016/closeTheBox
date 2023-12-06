import pygame
import random


def rollDice(screen, x1, y1, x2, y2, scale):
    roll = True
    count = 0
    clock = pygame.time.Clock()
    side1Image = pygame.image.load("die1.png").convert_alpha()
    side2Image = pygame.image.load("die2.png").convert_alpha()
    side3Image = pygame.image.load("die3.png").convert_alpha()
    side4Image = pygame.image.load("die4.png").convert_alpha()
    side5Image = pygame.image.load("die5.png").convert_alpha()
    side6Image = pygame.image.load("die6.png").convert_alpha()

    while roll:
        count += 1
        if count % 20 == 0:

            num1 = random.randrange(1, 7)
            # print("num1: ", num1)
            if num1 == 1:
                die1 = Dice(x1, y1, side1Image, scale)
                die1.draw(screen)
            elif num1 == 2:
                die1 = Dice(x1, y1, side2Image, scale)
                die1.draw(screen)
            elif num1 == 3:
                die1 = Dice(x1, y1, side3Image, scale)
                die1.draw(screen)
            elif num1 == 4:
                die1 = Dice(x1, y1, side4Image, scale)
                die1.draw(screen)
            elif num1 == 5:
                die1 = Dice(x1, y1, side5Image, scale)
                die1.draw(screen)
            elif num1 == 6:
                die1 = Dice(x1, y1, side6Image, scale)
                die1.draw(screen)

            num2 = random.randrange(1, 7)
            # print("num2: ", num2)
            if num2 == 1:
                die2 = Dice(x2, y2, side1Image, scale)
                die2.draw(screen)
            elif num2 == 2:
                die2 = Dice(x2, y2, side2Image, scale)
                die2.draw(screen)
            elif num2 == 3:
                die2 = Dice(x2, y2, side3Image, scale)
                die2.draw(screen)
            elif num2 == 4:
                die2 = Dice(x2, y2, side4Image, scale)
                die2.draw(screen)
            elif num2 == 5:
                die2 = Dice(x2, y2, side5Image, scale)
                die2.draw(screen)
            elif num2 == 6:
                die2 = Dice(x2, y2, side6Image, scale)
                die2.draw(screen)

        if count == 200:
            roll = False

        pygame.display.flip()
        clock.tick(100)
    dice = [die1, die2, num1+num2]
    return dice


class Dice:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen) -> None:
        screen.blit(self.image, (self.rect.x, self.rect.y))
