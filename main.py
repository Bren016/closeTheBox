import pygame
import button
import background
import tile
import dice
import box

pygame.init()
# SET SCREEN
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Close the Box")

# LOAD IMAGES
boxImage = pygame.image.load("box.png").convert_alpha()
gameBox = background.Background(100, 100, boxImage, 0.7)

submitImage = pygame.image.load("confirm.png").convert_alpha()
submit = button.Button(550, 350, submitImage, 1.5)

rollImage = pygame.image.load("roll.png").convert_alpha()
roll = button.Button(380, 535, rollImage, 0.6)

tile1Image = pygame.image.load("tile1.png").convert_alpha()
tile1 = tile.Tile(1, 220, 400, tile1Image, 0.7)
tile1HImage = pygame.image.load("tile1H.png").convert_alpha()
tile1H = button.Button(220, 400, tile1HImage, 0.7)
tile1DImage = pygame.image.load("down1.png").convert_alpha()
tile1D = background.Background(210, 450, tile1DImage, 0.7)

tile2Image = pygame.image.load("tile2.png").convert_alpha()
tile2 = tile.Tile(2, 283, 400, tile2Image, 0.7)
tile2HImage = pygame.image.load("tile2H.png").convert_alpha()
tile2H = button.Button(283, 400, tile2HImage, 0.7)
tile2DImage = pygame.image.load("down2.png").convert_alpha()
tile2D = background.Background(273, 450, tile1DImage, 0.7)

tile3Image = pygame.image.load("tile3.png").convert_alpha()
tile3 = tile.Tile(3, 346, 400, tile3Image, 0.7)
tile3HImage = pygame.image.load("tile3H.png").convert_alpha()
tile3H = button.Button(346, 400, tile3HImage, 0.7)
tile3DImage = pygame.image.load("down3.png").convert_alpha()
tile3D = background.Background(336, 450, tile1DImage, 0.7)

tile4Image = pygame.image.load("tile4.png").convert_alpha()
tile4 = tile.Tile(4, 409, 400, tile4Image, 0.7)
tile4HImage = pygame.image.load("tile4H.png").convert_alpha()
tile4H = button.Button(409, 400, tile4HImage, 0.7)
tile4DImage = pygame.image.load("down4.png").convert_alpha()
tile4D = background.Background(399, 450, tile1DImage, 0.7)

tile5Image = pygame.image.load("tile5.png").convert_alpha()
tile5 = tile.Tile(5, 472, 400, tile5Image, 0.7)
tile5HImage = pygame.image.load("tile5H.png").convert_alpha()
tile5H = button.Button(472, 400, tile5HImage, 0.7)
tile5DImage = pygame.image.load("down5.png").convert_alpha()
tile5D = background.Background(462, 450, tile1DImage, 0.7)

tile6Image = pygame.image.load("tile6.png").convert_alpha()
tile6 = tile.Tile(6, 535, 400, tile6Image, 0.7)
tile6HImage = pygame.image.load("tile6H.png").convert_alpha()
tile6H = button.Button(535, 400, tile6HImage, 0.7)
tile6DImage = pygame.image.load("down6.png").convert_alpha()
tile6D = background.Background(525, 450, tile1DImage, 0.7)

tile7Image = pygame.image.load("tile7.png").convert_alpha()
tile7 = tile.Tile(7, 598, 400, tile7Image, 0.7)
tile7HImage = pygame.image.load("tile7H.png").convert_alpha()
tile7H = button.Button(598, 400, tile7HImage, 0.7)
tile7DImage = pygame.image.load("down7.png").convert_alpha()
tile7D = background.Background(588, 450, tile1DImage, 0.7)

tile8Image = pygame.image.load("tile8.png").convert_alpha()
tile8 = tile.Tile(8, 661, 400, tile8Image, 0.7)
tile8HImage = pygame.image.load("tile8H.png").convert_alpha()
tile8H = button.Button(661, 400, tile8HImage, 0.7)
tile8DImage = pygame.image.load("down7.png").convert_alpha()
tile8D = background.Background(651, 449, tile1DImage, 0.7)

tile9Image = pygame.image.load("tile9.png").convert_alpha()
tile9 = tile.Tile(9, 724, 400, tile9Image, 0.7)
tile9HImage = pygame.image.load("tile9H.png").convert_alpha()
tile9H = button.Button(724, 400, tile9HImage, 0.7)
tile9DImage = pygame.image.load("down7.png").convert_alpha()
tile9D = background.Background(714, 448, tile1DImage, 0.7)

tile10Image = pygame.image.load("tile10.png").convert_alpha()
tile10 = tile.Tile(10, 787, 400, tile10Image, 0.7)
tile10HImage = pygame.image.load("tile10H.png").convert_alpha()
tile10H = button.Button(787, 400, tile10HImage, 0.7)
tile10DImage = pygame.image.load("down7.png").convert_alpha()
tile10D = background.Background(777, 447, tile1DImage, 0.7)

tile11Image = pygame.image.load("tile11.png").convert_alpha()
tile11 = tile.Tile(11, 850, 400, tile11Image, 0.7)
tile11HImage = pygame.image.load("tile11H.png").convert_alpha()
tile11H = button.Button(850, 400, tile11HImage, 0.7)
tile11DImage = pygame.image.load("down7.png").convert_alpha()
tile11D = background.Background(840, 446, tile1DImage, 0.7)

tile12Image = pygame.image.load("tile12.png").convert_alpha()
tile12 = tile.Tile(12, 913, 400, tile12Image, 0.7)
tile12HImage = pygame.image.load("tile12H.png").convert_alpha()
tile12H = button.Button(913, 400, tile12HImage, 0.7)
tile12DImage = pygame.image.load("down7.png").convert_alpha()
tile12D = background.Background(903, 445, tile1DImage, 0.7)

# INITIALIZE VARIABLES
rolls = []
hasRolled = False
rolled = 0
numbers = []
board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tiles = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, tile10, tile11, tile12]
tilesH = [tile1H, tile2H, tile3H, tile4H, tile5H, tile6H, tile7H, tile8H, tile9H, tile10H, tile11H, tile12H]
tilesD = [tile1D, tile2D, tile3D, tile4D, tile5D, tile6D, tile7D, tile8D, tile9D, tile10D, tile11D, tile12D]
canClick = False
gameOver = False
validate = False

run = True
while run:
    # INITIALIZE SCREEN
    screen.fill((30, 1, 1))
    pos = pygame.mouse.get_pos()

    # DRAW BACKGROUND
    gameBox.draw(screen)
    submit.draw(screen)
    roll.draw(screen)

    # DRAW TILES
    tile.drawTiles(tiles, tilesH, tilesD, screen)

    # GAME LOGIC
    if canClick and not gameOver:
        # UPDATE TILE STATE
        tile.update(tiles, tilesH, numbers, pos)

    if submit.isClicked(pos) and not submit.alreadyClicked:
        submit.alreadyClicked = True
        # CONFIRM SELECTION
        if box.isEqual(numbers, rolled):
            box.removeFromBoard(board, numbers)
            for num in numbers:
                num.isDown = True
            numbers.clear()
            canClick = False
        validate = False

        for value in numbers:
            print(value.getValue())

    if roll.isClicked(pos) and not roll.alreadyClicked:
        roll.alreadyClicked = True
        # ROLL DICE
        rolls = dice.rollDice(screen, 250, 520, 315, 520, 0.12)
        hasRolled = True
        canClick = True
        validate = True
        print(board)
        print(rolls[2])

    if hasRolled:
        # DISPLAY DICE
        rolls[0].draw(screen)
        rolls[1].draw(screen)
        rolled = rolls[2]

    if rolled != 0 and not box.possibleSolution(board, rolled) and validate:
        # GAME OVER
        gameOver = True
        print("GAME OVER")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # CLOSE SCREEN
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pos)
            pass

    pygame.display.update()

pygame.quit()
