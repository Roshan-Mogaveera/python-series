import pygame
import random

pygame.init()

# Screen
WIDTH = 600
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🏎️ Car Racing Game")

clock = pygame.time.Clock()

# Colors
GREEN = (40, 150, 60)
GRAY = (60, 60, 60)
WHITE = (255, 255, 255)
RED = (220, 40, 40)
BLUE = (40, 100, 220)
BLACK = (0, 0, 0)
YELLOW = (255, 220, 0)

# Road
road_x = 100
road_width = 400

# Player car
player_width = 50
player_height = 90

player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 130

player_speed = 7

# Enemy car
enemy_width = 50
enemy_height = 90

enemy_x = random.randint(
    road_x + 20,
    road_x + road_width - enemy_width - 20
)

enemy_y = -100

enemy_speed = 6

# Score
score = 0

font = pygame.font.Font(None, 40)

running = True

while running:

    # ---------------- EVENTS ----------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # ---------------- PLAYER MOVEMENT ----------------

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep car inside road

    if player_x < road_x:
        player_x = road_x

    if player_x > road_x + road_width - player_width:
        player_x = road_x + road_width - player_width

    # ---------------- ENEMY MOVEMENT ----------------

    enemy_y += enemy_speed

    # Enemy goes out of screen

    if enemy_y > HEIGHT:

        enemy_y = -100

        enemy_x = random.randint(
            road_x + 20,
            road_x + road_width - enemy_width - 20
        )

        score += 1

        # Increase difficulty

        if score % 5 == 0:
            enemy_speed += 1

    # ---------------- DRAW BACKGROUND ----------------

    screen.fill(GREEN)

    # Road

    pygame.draw.rect(
        screen,
        GRAY,
        (road_x, 0, road_width, HEIGHT)
    )

    # Road borders

    pygame.draw.rect(
        screen,
        WHITE,
        (road_x, 0, 8, HEIGHT)
    )

    pygame.draw.rect(
        screen,
        WHITE,
        (road_x + road_width - 8, 0, 8, HEIGHT)
    )

    # Road lane markings

    for y in range(0, HEIGHT, 80):

        pygame.draw.rect(
            screen,
            WHITE,
            (295, y, 10, 40)
        )

    # ---------------- DRAW PLAYER CAR ----------------

    pygame.draw.rect(
        screen,
        BLUE,
        (player_x, player_y, player_width, player_height)
    )

    # Windows

    pygame.draw.rect(
        screen,
        BLACK,
        (player_x + 10, player_y + 15, 30, 25)
    )

    # Wheels

    pygame.draw.rect(
        screen,
        BLACK,
        (player_x - 5, player_y + 15, 8, 25)
    )

    pygame.draw.rect(
        screen,
        BLACK,
        (player_x + player_width - 3, player_y + 15, 8, 25)
    )

    pygame.draw.rect(
        screen,
        BLACK,
        (player_x - 5, player_y + 55, 8, 25)
    )

    pygame.draw.rect(
        screen,
        BLACK,
        (player_x + player_width - 3, player_y + 55, 8, 25)
    )

    # ---------------- DRAW ENEMY CAR ----------------

    pygame.draw.rect(
        screen,
        RED,
        (enemy_x, enemy_y, enemy_width, enemy_height)
    )

    pygame.draw.rect(
        screen,
        BLACK,
        (enemy_x + 10, enemy_y + 15, 30, 25)
    )

    # ---------------- COLLISION ----------------

    player_rect = pygame.Rect(
        player_x,
        player_y,
        player_width,
        player_height
    )

    enemy_rect = pygame.Rect(
        enemy_x,
        enemy_y,
        enemy_width,
        enemy_height
    )

    if player_rect.colliderect(enemy_rect):

        print("💥 GAME OVER!")
        print("Your Score:", score)

        running = False

    # ---------------- SCORE ----------------

    score_text = font.render(
        "Score: " + str(score),
        True,
        YELLOW
    )

    screen.blit(score_text, (20, 20))

    pygame.display.update()

    clock.tick(60)

pygame.quit()