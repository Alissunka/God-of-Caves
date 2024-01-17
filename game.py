import pygame
import os

pygame.init()
screen_size = (1024, 576)
screen = pygame.display.set_mode(screen_size)
FPS = 60

clock = pygame.time.Clock()

pygame.mixer.music.load("unki-shteker.mp3")
pygame.mixer.music.set_volume(0.2)
button_sound = pygame.mixer.Sound("buttonsound.mp3")


icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

def draw_menu():
    pass

def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image

def start_screen():
    fon = pygame.transform.scale(load_image('fon.jpg'), screen_size)
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)

class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color1 = (218, 193, 144)
        self.color2 = (240, 233, 122)

    def draw(self, x, y, text, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(screen, self.color1, (x, y, self.width, self.height))
            if click[0] == 1:
                pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(350)
                if action is not None:
                    action()
        else:
            pygame.draw.rect(screen, self.color2, (x, y, self.width, self.height))

        print_text(text, x + 10, y + 10)

def run_game():
    start_screen()
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

        screen.fill((255, 255, 255))
        pygame.display.update()

def print_pause(message, x, y, font_color = (0, 0, 0), font_type = 'Font_Pause.ttf', font_size = 45):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))

def print_text(message, x, y, font_color = (0, 0, 0), font_type = 'Font_Pause.ttf', font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))

def pause():
    paused = True

    pygame.mixer.music.pause()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_pause('Пауза. Нажмите Enter.', 370, 250)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        clock.tick(20)

    pygame.mixer.music.unpause()

run_game()