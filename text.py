

def drawText(text, font, textCol, x, y, screen) -> None:
    img = font.render(text, True, textCol)
    screen.blit(img, (x, y))
