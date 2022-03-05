#import library
import pygame
pygame.init()
#There should be Npcs that tell you what to do, so you have motivaitoin. There should be bosses and a storyline, and you can collect coins and hearts, because you can take damage. You will only have 
# one life, and if all your hearts go down, you lose.
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
StrawberryWidth = 40
StrawberryHeight = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Strawberry climbing")

Bg_Image = pygame.image.load("sky-with-clouds-1.jpg").convert_alpha()
Charecter = pygame.image.load("p1_front.jpg").convert_alpha()
class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(Charecter, (45, 45))
        self.width = StrawberryWidth
        self.height = StraberryHeight
        self.rect = pygame.Rect(45, 45, self.width, self.height)
        self.rect.center = (x, y)
    def draw():
        screen.blit(self.image, (self.rect.x-12, self.rect.y-5))
clock = pygame.time.Clock()
run = True
while run:
    screen.blit(Bg_Image,(0,0))
    screen.blit(Charecter, (45, 45))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
