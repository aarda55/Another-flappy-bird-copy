import pygame
import random
import time

pygame.init()

# set up the screen
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Flappy Bird")

# load the images
background = pygame.image.load("sprites/background.png").convert()
bird = pygame.image.load("sprites/bird.png").convert_alpha()
pipe_top = pygame.image.load("sprites/pipe_top.png").convert_alpha()
pipe_bottom = pygame.image.load("sprites/pipe_bottom.png").convert_alpha()

# set up the game variables
bird_x = 50
bird_y = 300
bird_speed = 0
gravity = 0.25
score = 0
font = pygame.font.Font(None, 36)

# create the pipes
pipes = []
for i in range(3):
    pipe_x = 500 + i * 200
    pipe_y = random.randint(150, 450)
    pipes.append([pipe_x, pipe_y])

# main game loop
running = True
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = -5

    # update the game state
    bird_speed += gravity
    bird_y += bird_speed
    for pipe in pipes:
        pipe[0] -= 2
        if pipe[0] < -80:
            pipe[0] = 500
            pipe[1] = random.randint(150, 450)
        if bird_x + 30 > pipe[0] and bird_x < pipe[0] + 80:
            if bird_y < pipe[1] + 300 or bird_y + 30 > pipe[1] + 400:
                running = False
        if bird_y > 570 or bird_y < 0:
            running = False
        if pipe[0] == bird_x:
            score += 1

    # draw the game objects
    screen.blit(background, (0, 0))
    for pipe in pipes:
        screen.blit(pipe_top, (pipe[0], pipe[1] - 600))
        screen.blit(pipe_bottom, (pipe[0], pipe[1] + 200))
    screen.blit(bird, (bird_x, bird_y))
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()