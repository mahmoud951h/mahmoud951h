import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GROUND_HEIGHT = 50
WHITE = (255, 255, 255)
PLAYER_SPEED = 5
GRAVITY = 1
JUMP_STRENGTH = -15

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario-like Game")

# Create fonts
font = pygame.font.Font(None, 36)

# Create the player
player = pygame.Rect(50, HEIGHT - GROUND_HEIGHT - 50, 40, 60)
player_speed_x, player_speed_y = 0, 0
is_jumping = False

# Create the ground
ground = pygame.Rect(0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_speed_x = -PLAYER_SPEED
    elif keys[pygame.K_RIGHT]:
        player_speed_x = PLAYER_SPEED
    else:
        player_speed_x = 0

    if keys[pygame.K_SPACE] and not is_jumping:
        player_speed_y = JUMP_STRENGTH
        is_jumping = True

    player_speed_y += GRAVITY
    player.y += player_speed_y

    if player.colliderect(ground):
        is_jumping = False
        player.y = HEIGHT - GROUND_HEIGHT - player.height
        player_speed_y = 0

    player.x += player_speed_x

    # Prevent player from going out of the screen
    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the ground and player
    pygame.draw.rect(screen, (0, 255, 0), ground)
    pygame.draw.rect(screen, (0, 0, 255), player)

    # Update the screen
    pygame.display.update()
