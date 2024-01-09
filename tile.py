import pygame


def drawTiles(tiles, tilesH, tilesD, screen):
    for tile in range(len(tiles)):
        if not tiles[tile].isHighlighted() and not tiles[tile].isDown:
            tiles[tile].draw(screen)
        elif tiles[tile].isHighlighted() and not tiles[tile].isDown:
            tilesH[tile].draw(screen)
        else:
            tilesD[tile].draw(screen)


def update(tiles, tilesH, numbers, pos):
    for tile in range(len(tiles)):
        if tiles[tile].isClicked(pos) and not tiles[tile].alreadyClicked and not tiles[tile].isDown:
            tiles[tile].alreadyClicked = True
            numbers.append(tiles[tile])
        if tilesH[tile].isClicked(pos) and not tilesH[tile].alreadyClicked and not tiles[tile].isDown:
            tilesH[tile].alreadyClicked = True
            tilesH[tile].counter += 1
        if tilesH[tile].isClicked(pos) and tilesH[tile].counter == 2 and not tiles[tile].isDown:
            tiles[tile].removeHighlighter()
            numbers.remove(tiles[tile])
            numbers.remove(tiles[tile])
            tilesH[tile].counter = 0


class Tile:
    def __init__(self, value: int, x, y, image, scale) -> None:
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.alreadyClicked = False
        self.value = value
        self.highlighted = False
        self.isDown = False

    def resetTile(self) -> None:
        self.clicked = False
        self.alreadyClicked = False
        self.highlighted = False
        self.isDown = False

    def draw(self, screen) -> None:
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def isClicked(self, pos) -> bool:
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                self.highlighted = True

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
            self.alreadyClicked = False

        return self.clicked

    def getValue(self) -> int:
        return self.value

    def isHighlighted(self) -> bool:
        return self.highlighted

    def removeHighlighter(self) -> None:
        self.highlighted = False
