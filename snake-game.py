import pygame
import random

pygame.init()

# Screen
WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

clock = pygame.time.Clock()

# Colors
BLACK = (20, 20, 20)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 120, 0)
RED = (220, 40, 40)
WHITE = (255, 255, 255)

# Snake settings
BLOCK = 20

snake = [
    [300, 300],
    [280, 300],
    [260, 300]
]

direction = "RIGHT"

# Food
food = [
    random.randrange(0, WIDTH, BLOCK),
    random.randrange(0, HEIGHT, BLOCK)
]

score = 0

font = pygame.font.Font(None, 40)
game_over_font = pygame.font.Font(None, 70)

running = True

while running:

    # ---------------- EVENTS ----------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"

            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"

            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"

            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # ---------------- MOVE SNAKE ----------------

    head = snake[0].copy()

    if direction == "UP":
        head[1] -= BLOCK

    elif direction == "DOWN":
        head[1] += BLOCK

    elif direction == "LEFT":
        head[0] -= BLOCK

    elif direction == "RIGHT":
        head[0] += BLOCK

    snake.insert(0, head)

    # ---------------- EAT FOOD ----------------

    if head == food:

        score += 1

        food = [
            random.randrange(0, WIDTH, BLOCK),
            random.randrange(0, HEIGHT, BLOCK)
        ]

    else:
        snake.pop()

    # ---------------- COLLISION ----------------

    # Hit wall
    if (
        head[0] < 0
        or head[0] >= WIDTH
        or head[1] < 0
        or head[1] >= HEIGHT
    ):
        running = False

    # Hit itself
    if head in snake[1:]:
        running = False

    # ---------------- DRAW ----------------

    screen.fill(BLACK)

    # Draw snake
    for i, segment in enumerate(snake):

        if i == 0:
            pygame.draw.rect(
                screen,
                DARK_GREEN,
                (segment[0], segment[1], BLOCK, BLOCK)
            )
        else:
            pygame.draw.rect(
                screen,
                GREEN,
                (segment[0], segment[1], BLOCK, BLOCK)
            )

    # Draw food
    pygame.draw.rect(
        screen,
        RED,
        (food[0], food[1], BLOCK, BLOCK)
    )

    # Score
    score_text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(score_text, (10, 10))

    pygame.display.update()

    clock.tick(10 + score // 5)


# ---------------- GAME OVER ----------------

screen.fill(BLACK)

game_over = game_over_font.render(
    "GAME OVER",
    True,
    RED
)

final_score = font.render(
    "Score: " + str(score),
    True,
    WHITE
)

screen.blit(
    game_over,
    (WIDTH // 2 - game_over.get_width() // 2, 230)
)

screen.blit(
    final_score,
    (WIDTH // 2 - final_score.get_width() // 2, 310)
)

pygame.display.update()

pygame.time.wait(3000)

pygame.quit()