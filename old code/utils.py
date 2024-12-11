import pygame
import os

DEF_PATH = 'Images/'

def load_image(path):
    img = pygame.image.load(DEF_PATH+path).convert_alpha()
    return img

def load_images(path):
    images = []
    for image in os.listdir(DEF_PATH+path):
        images.append(load_image(path + '/' + image))
    return images


