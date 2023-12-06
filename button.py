import pygame


class Button:
    def __init__(self, x, y, image, scale) -> None:
        self.displayed = True
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.alreadyClicked = False
        self.counter = 0

    def draw(self, screen) -> None:
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def isClicked(self, pos) -> bool:
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                print("clicked")

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
            self.alreadyClicked = False

        return self.clicked

    def isDisplayed(self) -> bool:
        return self.displayed

    def dontDisplay(self):
        self.displayed = False
