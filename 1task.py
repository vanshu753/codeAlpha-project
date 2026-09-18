# Install first: pip install pygame

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Treasure Hunt")

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

places = {
    1: "Forest",
    2: "Cave",
    3: "Mountain",
    4: "River",
    5: "Temple"
}

score = 0
treasure = random.randint(1, 5)
trap = random.randint(1, 5)

while trap == treasure:
    trap = random.randint(1, 5)

running = True

while running:
    screen.fill((240, 240, 240))

    title = font.render("Treasure Hunt", True, (0, 0, 0))
    screen.blit(title, (300, 40))

    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (30, 30))

    for i, place in places.items():
        text = font.render(str(i) + " - " + place, True, (0, 0, 0))
        screen.blit(text, (300, 100 + i * 50))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                choice = 1
            elif event.key == pygame.K_2:
                choice = 2
            elif event.key == pygame.K_3:
                choice = 3
            elif event.key == pygame.K_4:
                choice = 4
            elif event.key == pygame.K_5:
                choice = 5
            else:
                choice = 0

            if choice:
                if choice == treasure:
                    score += 100
                    treasure = random.randint(1, 5)

                elif choice == trap:
                    score -= 30
                    trap = random.randint(1, 5)

                while trap == treasure:
                    trap = random.randint(1, 5)

    pygame.display.update()
    clock.tick(60)

pygame.quit()