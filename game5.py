import pygame
import sys
import random

pygame.init()

# setup basics
WIDTH, HEIGHT = 800, 600
FPS = 120
WHITE = (255, 255, 255)

# creating the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Forest Run")

# visuals of th game
background_image = pygame.image.load("forest.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

girl_image = pygame.image.load("girl.png")
girl_image = pygame.transform.scale(girl_image, (75, 75))

monster_image = pygame.image.load("monster2.png")
monster_image = pygame.transform.scale(monster_image, (50, 50))

# player settings
player_size = 75
player_speed = 5

# monster settings
monster_size = 50
monster_speed = 5

# initial player position
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 20

# initial number of lives
lives = 3

# clock to control the frame rate
clock = pygame.time.Clock()

# list to store monsters
monsters = []

# Game loop
while lives > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # spawn monsters
    if random.randint(0, 100) < 5:
        monster_x = random.randint(0, WIDTH - monster_size)
        monster_y = 0
        monsters.append([monster_x, monster_y])

    # move monsters
    for monster in monsters:
        monster[1] += monster_speed

    # touch monsters
    for monster in monsters:
        if (
            player_x < monster[0] + monster_size
            and player_x + player_size > monster[0]
            and player_y < monster[1] + monster_size
            and player_y + player_size > monster[1]
        ):
            # reduce lives on collision
            lives -= 1
            print(f"Remaining Lives: {lives}")
            monsters = []  
            pygame.time.delay(1000)  

    # remove monsters that have gone off the screen
    monsters = [monster for monster in monsters if monster[1] < HEIGHT]

    # background
    screen.blit(background_image, (0, 0))

    # monsters
    for monster in monsters:
        screen.blit(monster_image, (monster[0], monster[1]))

    # player
    screen.blit(girl_image, (player_x, player_y))

    # update the display
    pygame.display.flip()

    # frame rate
    clock.tick(FPS)

# game over at the end
font = pygame.font.Font(None, 36)
game_over_text = font.render("Game Over!!!XD", True, WHITE)
screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 18))
pygame.display.flip()

# delay for end
pygame.time.delay(3000)
pygame.quit()
sys.exit()
