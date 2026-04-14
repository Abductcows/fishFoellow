import numpy as np
import pygame

#Surface defs init
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Pygame Test')
test_surface = pygame.Surface((1200, 800))
test_surface.fill("white")
cent_surf = pygame.Surface((100,100))
cent_rect = screen.get_rect().center
cent_surf_rect = cent_surf.get_rect(center=screen.get_rect().center)
pygame.draw.circle(test_surface, 'black', center=test_surface.get_rect().center, radius=300, width=6)

def cfactor():
    targxy = test_surface.get_size()
    dispxy = screen.get_size()
    destxy = ( (dispxy[0] - targxy[0])/2, (dispxy[1] - targxy[1])/2)
    return destxy

def createarena(rad = 30): # rad in cm, pos X = cx + r*cos(θ), assuming cx = cy = 0
    coords = []
        #area = math.pi * rad ** 2
        #circumference = 2 * math.pi * rad
        #diameter = 2*rad
    theta = np.linspace(0,2*np.pi, 1000) #
    for i, angle in enumerate(theta):
        x = rad * np.cos(theta[i])
        y = rad * np.sin(theta[i])
        coords.append([x,y])
    return coords


print('hi')












