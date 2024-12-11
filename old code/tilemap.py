import pygame
from settings import *

NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]

class Tileset:
    def __init__(self,game):
        self.game = game
        self.tile_size = 32
        self.tilemap = {}
        self.offgrid_tiles = []
        for i in range(50):
            x = i-25
            self.tilemap[str(x) + ';' + str(5)] = {'block':'grass', 'pos':(x,6)}
            for o in range(20):
                y = o+7
                self.tilemap[str(x) + ';' + str(y)] = { 'block':'stone', 'pos':(x,y)}
    
    def tiles_around(self,player_pos):
        tiles = []
        player_tile = (int(player_pos[0] // self.tile_size), int(player_pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            check_loc = str(player_tile[0] + offset[0]) + ';' + str(player_tile[1] + offset[1])
            if check_loc in self.tilemap:
               tiles.append(self.tilemap[check_loc])
        return tiles
    def rects_around(self,pos):
        rects = []
        for tile in self.tiles_around(pos):
            rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects

    def render(self, surf, offset):
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(pygame.transform.scale_by(self.game.assets[tile['block']],2),(tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))