import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚀 Space Shooter")

# Colors
WHITE = (255, 255, 255)
BLACK = (5, 5, 20)
BLUE = (50, 150, 255)
RED = (255, 60, 60)
YELLOW = (255, 220, 50)
GREEN = (50, 255, 100)
PURPLE = (180, 50, 255)

# Clock
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 70)


# ---------------- PLAYER ----------------

player_width = 50
player_height = 40

player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 70

player_speed = 7

lives = 3
score = 0


# ---------------- BULLETS ----------------

bullets = []

bullet_width = 5
bullet_height = 15
bullet_speed = 10


# ---------------- ENEMIES ----------------

enemies = []

enemy_width = 45
enemy_height = 35
enemy_speed = 3


# Create stars
stars = []

for i in range(100):
    stars.append([
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT),
        random.randint(1, 3)
    ])


# ---------------- FUNCTIONS ----------------

def draw_player(x, y):
    # Main spaceship
    pygame.draw.polygon(
        screen,
        BLUE,
        [
            (x + player_width // 2, y),
            (x, y + player_height),
            (x + player_width // 2, y + player_height - 10),
            (x + player_width, y + player_height)
        ]
    )

    # Cockpit
    pygame.draw.circle(
        screen,
        WHITE,
        (x + player_width // 2, y + 18),
        6
    )


def draw_enemy(x, y):
    # Enemy body
    pygame.draw.rect(
        screen,
        RED,
        (x + 5, y + 10, enemy_width - 10, enemy_height - 10)
    )

    # Enemy wings
    pygame.draw.polygon(
        screen,
        PURPLE,
        [
            (x, y + enemy_height),
            (x + 10, y + 10),
            (x + enemy_width // 2, y + 20),
            (x + enemy_width - 10, y + 10),
            (x + enemy_width, y + enemy_height)
        ]
    )

    # Eyes
    pygame.draw.circle(
        screen,
        YELLOW,
        (x + 15, y + 20),
        4
    )

    pygame.draw.circle(
        screen,
        YELLOW,
        (x + enemy_width - 15, y + 20),
        4
    )


def create_enemy():
    x = random.randint(0, WIDTH - enemy_width)
    y = random.randint(-100, -40)

    enemies.append([x, y])


def show_text(text, font_used, color, x, y):
    message = font_used.render(text, True, color)
    screen.blit(message, (x, y))


def game_over():
    screen.fill(BLACK)

    show_text(
        "GAME OVER",
        big_font,
        RED,
        WIDTH // 2 - 160,
        HEIGHT // 2 - 80
    )

    show_text(
        f"Final Score: {score}",
        font,
        WHITE,
        WIDTH // 2 - 90,
        HEIGHT // 2
    )

    show_text(
        "Press R to Restart",
        font,
        YELLOW,
        WIDTH // 2 - 110,
        HEIGHT // 2 + 50
    )

    pygame.display.update()


# ---------------- GAME LOOP ----------------

running = True
game_finished = False

enemy_timer = 0

while running:

    clock.tick(60)

    # ---------------- EVENTS ----------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Shoot bullet
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and not game_finished:

                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y

                bullets.append([bullet_x, bullet_y])

            # Restart
            if event.key == pygame.K_r and game_finished:

                player_x = WIDTH // 2 - player_width // 2

                bullets.clear()
                enemies.clear()

                score = 0
                lives = 3
                enemy_speed = 3

                game_finished = False


    # ---------------- GAME LOGIC ----------------

    if not game_finished:

        keys = pygame.key.get_pressed()

        # Move left
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= player_speed

        # Move right
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += player_speed

        # Keep player inside screen
        if player_x < 0:
            player_x = 0

        if player_x > WIDTH - player_width:
            player_x = WIDTH - player_width


        # ---------------- BULLET MOVEMENT ----------------

        for bullet in bullets[:]:

            bullet[1] -= bullet_speed

            # Remove bullet if it leaves screen
            if bullet[1] < 0:
                bullets.remove(bullet)


        # ---------------- CREATE ENEMIES ----------------

        enemy_timer += 1

        if enemy_timer > 35:
            create_enemy()
            enemy_timer = 0


        # ---------------- ENEMY MOVEMENT ----------------

        for enemy in enemies[:]:

            enemy[1] += enemy_speed

            # Enemy reaches bottom
            if enemy[1] > HEIGHT:

                enemies.remove(enemy)

                lives -= 1

                if lives <= 0:
                    game_finished = True


        # ---------------- COLLISION ----------------

        for bullet in bullets[:]:

            bullet_rect = pygame.Rect(
                bullet[0],
                bullet[1],
                bullet_width,
                bullet_height
            )

            for enemy in enemies[:]:

                enemy_rect = pygame.Rect(
                    enemy[0],
                    enemy[1],
                    enemy_width,
                    enemy_height
                )

                if bullet_rect.colliderect(enemy_rect):

                    if bullet in bullets:
                        bullets.remove(bullet)

                    if enemy in enemies:
                        enemies.remove(enemy)

                    score += 10

                    # Increase difficulty
                    if score % 100 == 0:
                        enemy_speed += 0.5

                    break


        # ---------------- PLAYER COLLISION ----------------

        player_rect = pygame.Rect(
            player_x,
            player_y,
            player_width,
            player_height
        )

        for enemy in enemies[:]:

            enemy_rect = pygame.Rect(
                enemy[0],
                enemy[1],
                enemy_width,
                enemy_height
            )

            if player_rect.colliderect(enemy_rect):

                enemies.remove(enemy)

                lives -= 1

                if lives <= 0:
                    game_finished = True


        # ---------------- DRAW EVERYTHING ----------------

        screen.fill(BLACK)

        # Stars
        for star in stars:

            pygame.draw.circle(
                screen,
                WHITE,
                (star[0], star[1]),
                star[2]
            )

            star[1] += star[2]

            if star[1] > HEIGHT:
                star[1] = 0
                star[0] = random.randint(0, WIDTH)


        # Draw player
        draw_player(player_x, player_y)


        # Draw bullets
        for bullet in bullets:

            pygame.draw.rect(
                screen,
                YELLOW,
                (
                    bullet[0],
                    bullet[1],
                    bullet_width,
                    bullet_height
                )
            )


        # Draw enemies
        for enemy in enemies:
            draw_enemy(enemy[0], enemy[1])


        # Score
        show_text(
            f"Score: {score}",
            font,
            WHITE,
            20,
            20
        )

        # Lives
        show_text(
            f"Lives: {lives}",
            font,
            GREEN,
            WIDTH - 120,
            20
        )

        pygame.display.update()


    else:

        game_over()


pygame.quit()
sys.exit()