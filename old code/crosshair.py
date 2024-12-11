import pygame

class Crosshair:
    def __init__(self):
        self.tile = (0,0)
        self.rect = pygame.Rect(self.tile,(32,32))
    def crosshair(self,mouse_loc,surf,offset):
        self.tile = ((mouse_loc[0]) // 64 * 32,(mouse_loc[1]) // 64 * 32)
        self.rect = pygame.Rect(self.tile,(32,32))
        pygame.draw.rect(surf,'white',self.rect,2)

