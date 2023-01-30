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

# Creating text title
test_font = pygame.font.Font('fonts/PixelType.ttf', 120)

ground = pygame.image.load('graphics/Ground.png')
ground_scaled = pygame.transform.scale(ground, (1280, 720))
text = test_font.render('SMASH!', False, 'White')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(ground_scaled, (0,500))
    screen.blit(text, (520, 90))
    
    pygame.display.update()
    clock.tick(144)