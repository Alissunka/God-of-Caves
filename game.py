import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('God of Caves')

pygame.mixer.music.load("unki-shteker.mp3")
pygame.mixer.music.set_volume(0.5)

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


def run_game():
    pygame.mixer.music.play(-1)
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pause()

        display.fill((255, 255, 255))
        pygame.display.update()

def print_pause(message, x, y, font_color = (0, 0, 0), font_type = 'Font_Pause.ttf', font_size = 36):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))

def pause():
    paused = True

    pygame.mixer.music.pause()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_pause('Пауза. Нажмите Enter', 270, 270)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        clock.tick(20)

    pygame.mixer.music.unpause()

run_game()