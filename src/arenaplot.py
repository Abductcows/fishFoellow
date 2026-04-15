import numpy as np
import pygame

# Surface defs init
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Pygame Test')
test_surface = pygame.Surface((1200, 1200))
test_surface.fill("white")
pygame.draw.circle(test_surface, 'black', center=test_surface.get_rect().center, radius=350, width=6)


def cfactor():
    targxy = test_surface.get_size()
    dispxy = screen.get_size()
    destxy = ((dispxy[0] - targxy[0]) / 2, (dispxy[1] - targxy[1]) / 2)
    return destxy


def createarena(rad=30):  # rad in px, pos X = cx + r*cos(θ), assuming cx = cy = 0
    coords = []
    # area = math.pi * rad ** 2
    # circumference = 2 * math.pi * rad
    # diameter = 2*rad
    theta = np.linspace(0, 2 * np.pi, 1000)  #
    return [(rad * np.cos(angle), rad * np.sin(angle)) for angle in theta]

# Offset and add cx and cy to x,y coords (Remove negative numbers)

print('hi')

if __name__ == '__main__':
    createarena()
    coords = createarena()
    print('hi')