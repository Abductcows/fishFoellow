from sys import exit
# Project modules
import arenaplot as aplot
from arenaplot import *

pygame.init()
clock = pygame.time.Clock()



while True:
    for event in pygame.event.get(): # Event loop
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(test_surface, cfactor())
    pygame.display.flip()

    pygame.display.update()
    clock.tick(60)

