import pygame

class Crosshair:
    def __init__(self):
        self.tile = (0,0)
        self.rect = pygame.FRect(self.tile[0] * 16, self.tile[1] * 16, 16, 16)
    def update(self, mouse_loc, surf, offset):
        self.tile = (mouse_loc[0] // 16,mouse_loc[1] // 16)
        self.rect = pygame.FRect(self.tile[0] * 16 - offset[0] % 16, self.tile[1] * 16 - offset[1] % 16, 16, 16)
        pygame.draw.rect(surf, 'white', self.rect, 2)