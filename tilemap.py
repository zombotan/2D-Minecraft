import pygame
from settings import *

NEIGHBOR_OFFSETS = [(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1),(-1,-1),(0,-1),(1,-1),(0,2),(0,-2),(1,2),(1,-2),(-1,2),(-1,-2),(2,2),(2,-2),(-2,2),(-2,-2),(2,0),(-2,0),(2,1),(-2,1),(2,-1),(-2,-1)]
PHYSICS_TILES = {'grass', 'stone'}

class Tilemap:
    def __init__(self,renderer, tile_size = 16) :
        self.tile_size = tile_size
        self.renderer = renderer
        self.tilemap = {}
        self.offgrid_tiles = []
        for i in range(1000):
            self.tilemap[str(i) + ';-1'] = {'block': 'grass','pos' :(i, -1)}
            for iy in range(1000):
                self.tilemap[str(i) + ';' + str(iy)] = {'block' : 'stone', 'pos' :(i,iy)}        
                        
    def tiles_around(self,pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size),int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            chech_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if chech_loc in self.tilemap:
                tiles.append(self.tilemap[chech_loc])
        return tiles
    
    def rects_around(self,pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['block'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects     
    
    def break_block(self,pos):
        tile_loc = (int(pos[0] // self.tile_size),int(pos[1] // self.tile_size))
        self.tilemap.pop(str(tile_loc[0]) + ';' + str(tile_loc[1]),"not found")
        
    def render(self,surf, offset = (0,0)):
        for x in range(offset[0] // self.tile_size,(offset[0] + surf.get_width()) // self.tile_size + 1):
            for y in range(offset[1] // self.tile_size, (offset[1] + surf.get_height()) // self.tile_size + 1):
                loc = str(x) + ';' + str(y)
                if loc in self.tilemap:
                    tile = self.tilemap[loc]
                    surf.blit(self.renderer.assets[tile['block']], (tile['pos'][0] * self.tile_size - offset[0],tile['pos'][1] * self.tile_size - offset[1]))
                
        #for loc in self.tilemap:
        #    tile = self.tilemap[loc]
        #    surf.blit(self.renderer.assets[tile['block']], (tile['pos'][0] * self.tile_size - offset[0],tile['pos'][1] * self.tile_size - offset[1]))
            
        #for tile in self.offgrid_tiles:
        #    surf.blit(self.renderer.assets[tile['block']], (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))