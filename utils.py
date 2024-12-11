import pygame
import os

DEF_PATH = 'Images/'

def load_image(path):
    img = pygame.image.load(DEF_PATH + path).convert_alpha()
    return img
