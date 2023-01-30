import pygame
from sys import exit

# opposite of pygame.quit()
pygame.init()

# sets screen size
screen = pygame.display.set_mode((1280, 720))

# game name
pygame.display.set_caption("SMASH!")

# set framerate
clock = pygame.time.Clock()

# Surfaces
# Creating text title
test_font = pygame.font.Font('fonts/PixelType.ttf', 120)
text = test_font.render('SMASH!', False, 'Dark Green')

ground = pygame.image.load('graphics/Ground.png').convert()
ground_scaled = pygame.transform.scale(ground, (1280, 720))
sky = pygame.image.load('graphics/Sky.png').convert()
sky_scaled = pygame.transform.scale(sky, (1280, 720))

dummy_surface = pygame.image.load('graphics/dummy.png').convert_alpha()
dummy_scaled = pygame.transform.scale(dummy_surface, (400, 300))
dummy_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_scaled, (0,0))
    screen.blit(ground_scaled, (0,500))
    screen.blit(text, (520, 90))

    dummy_x_pos -= 1
    if dummy_x_pos < -300: dummy_x_pos = 1300
    screen.blit(dummy_scaled, (dummy_x_pos, 250))
    
    pygame.display.update()
    clock.tick(144)