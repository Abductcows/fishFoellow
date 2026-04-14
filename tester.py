import pygame
from sys import exit
import numpy as np






pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Pygame Test')
clock = pygame.time.Clock()

#Surface defs
test_surface = pygame.Surface((1200, 800))
cent_surf = pygame.Surface((100,100))
def cfactor():
    targxy = test_surface.get_size()
    dispxy = screen.get_size()
    destxy = ( (dispxy[0] - targxy[0])/2, (dispxy[1] - targxy[1])/2)
    return destxy

test_surface.fill(("white"))
cent_rect = screen.get_rect().center
cent_surf_rect = cent_surf.get_rect(center=screen.get_rect().center)

pygame.draw.circle(test_surface, 'black', center=test_surface.get_rect().center, radius=300, width=np.random.randint(6,7))
while True:
    for event in pygame.event.get(): # Event loop
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, cfactor())
    pygame.display.flip()

    pygame.display.update()
    clock.tick(60)


# with open('data/KOTrials_Set10_24hrA_7.14.25_LocationOutput.csv', newline='') as csvfile:
#     csvfile.seek(0)
#     fishreader = csv.reader(csvfile, dialect='excel')
#     for irow, row in enumerate(fishreader):
# #        if irow > 0:
#       print(', '.join(row[6:9]))  # Access (frame, X, Y fields)
#       if irow == 10:
#             break
#
# def readfiles():
#     files = []
#     for i,filename in enumerate(os.listdir('data')):
#         files.append(i)
#         rd = pd.read_csv(os.path.join('data', filename), sep=',')
#         files[i] = rd
#     return files
#
# csvlist = readfiles()

# f1 = pd.read_csv("data/KOTrials_Set10_24hrA_7.14.25_LocationOutput.csv")
# f2 = pd.read_csv("data/KOTrials_Set10_24hrB_7.8.25_LocationOutput.csv")
# f3 = pd.read_csv("data/KOTrials_Set10_24hrC_7.8.25_LocationOutput.csv")

def readfiles():
    files = []
    for i,filename in enumerate(os.listdir('data')):
        files.append(i)
        rd = pd.read_csv(os.path.join('data', filename), sep=',')
        files[i] = rd
    return files

csvlist = readfiles()



