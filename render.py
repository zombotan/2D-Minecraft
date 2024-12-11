import pygame
from settings import *
from utils import *
from tilemap import Tilemap
from player import Player
from crosshair import Crosshair

class Renderer:
    def __init__(self,screen):
        self.screen = screen
        self.assets = {
			'grass': load_image('tiles/grass.png'),
			'stone': load_image('tiles/stone.png'),
			'cobblestone': load_image('tiles/cobblestone.png'),
			'bedrock': load_image('tiles/bedrock.png'),
			'block_diamond': load_image('tiles/block_diamond.png'),
			'block_gold': load_image('tiles/block_gold.png'),
			'block_iron': load_image('tiles/block_iron.png'),
			'bookshelf': load_image('tiles/bookshelf.png'),
			'brick': load_image('tiles/brick.png'),
			'cactus': load_image('tiles/cactus.png'),
			'chest_double_left': load_image('tiles/chest_double_left.png'),
			'chest_double_right': load_image('tiles/chest_double_right.png'),
			'chest_single': load_image('tiles/chest_single.png'),
			'clay': load_image('tiles/clay.png'),
			'cobweb': load_image('tiles/cobweb.png'),
			'crafting_table': load_image('tiles/crafting_table.png'),
			'crying_obsidian': load_image('tiles/crying_obsidian.png'),
			'dandelion': load_image('tiles/dandelion.png'),
			'diorite': load_image('tiles/diorite.png'),
			'dirt': load_image('tiles/dirt.png'),
			'farmgrass_wet': load_image('tiles/farmgrass_wet.png'),
			'furnace_lit': load_image('tiles/furnace_lit.png'),
			'furnace': load_image('tiles/furnace.png'),
			'farmgrass': load_image('tiles/farmgrass.png'),
			'glass': load_image('tiles/glass.png'),
			'grass_snow': load_image('tiles/grass_snow.png'),
			'gravel': load_image('tiles/gravel.png'),
			'ice': load_image('tiles/ice.png'),
			'iron_door_up': load_image('tiles/iron_door_up.png'),
			'ladder': load_image('tiles/ladder.png'),
			'mossy_cobble': load_image('tiles/mossy_cobble.png'),
			'mushroom_red': load_image('tiles/mushroom_red.png'),
			'mushroom_brown': load_image('tiles/mushroom_brown.png'),
			'music_box': load_image('tiles/music_box.png'),
			'oak_log': load_image('tiles/oak_log.png'),
			'obsidian': load_image('tiles/obsidian.png'),
			'ore_coal': load_image('tiles/ore_coal.png'),
			'ore_gold': load_image('tiles/ore_gold.png'),
			'ore_iron': load_image('tiles/ore_iron.png'),
			'ore_diamond': load_image('tiles/ore_diamond.png'),
			'ore_redstone': load_image('tiles/ore_redstone.png'),
			'rose': load_image('tiles/rose.png'),
			'sand': load_image('tiles/sand.png'),
			'sexy_stone': load_image('tiles/sexy_stone.png'),
			'snow': load_image('tiles/snow.png'),
			'spawner': load_image('tiles/spawner.png'),
			'sponge': load_image('tiles/sponge.png'),
			'sugar_cane': load_image('tiles/sugar_cane.png'),
			'tnt': load_image('tiles/tnt.png'),
			'torch': load_image('tiles/torch.png'),
			'tree_sapling': load_image('tiles/tree_sapling.png'),
			'water': load_image('tiles/water.png'),
			'wood_door_up': load_image('tiles/wood_door_up.png'),
			'wood_plank': load_image('tiles/wood_plank.png'),
			'wool_white': load_image('tiles/wool_white.png'),
			'bed_left': load_image('tiles/bed_left.png'),
			'bed_right': load_image('tiles/bed_right.png'),
			'birch_log': load_image('tiles/birch_log.png'),
			'block_lapis': load_image('tiles/block_lapis.png'),
			'cake_item': load_image('tiles/cake_item.png'),
			'cake': load_image('tiles/cake.png'),
			'carved_pumpkin': load_image('tiles/carved_pumpkin.png'),
			'dark_oak_log': load_image('tiles/dark_oak_log.png'),
			'glowstone': load_image('tiles/glowstone.png'),
			'iron_door_down': load_image('tiles/iron_door_down.png'),
			'jack_o_lantern': load_image('tiles/jack_o_lantern.png'),
			'lava_1': load_image('tiles/lava_1.png'),
			'lava_2': load_image('tiles/lava_2.png'),
			'lava_3': load_image('tiles/lava_3.png'),
			'lava_4': load_image('tiles/lava_4.png'),
			'lava_5': load_image('tiles/lava_5.png'),
			'netherrack': load_image('tiles/netherrack.png'),
			'ore_lapis': load_image('tiles/ore_lapis.png'),
			'pumpkin': load_image('tiles/pumpkin.png'),
			'sand_2': load_image('tiles/sand_2.png'),
			'sand_3': load_image('tiles/sand_3.png'),
			'sandstone': load_image('tiles/sandstone.png'),
			'soul_sand': load_image('tiles/soul_sand.png'),
			'stone_break1': load_image('tiles/stone_break1.png'),
			'stone_break2': load_image('tiles/stone_break2.png'),
			'stone_break3': load_image('tiles/stone_break3.png'),
			'stone_break4': load_image('tiles/stone_break4.png'),
			'stone_break5': load_image('tiles/stone_break5.png'),
			'stone_break6': load_image('tiles/stone_break6.png'),
			'stone_break7': load_image('tiles/stone_break7.png'),
			'stone_break8': load_image('tiles/stone_break8.png'),
			'stone_break9': load_image('tiles/stone_break9.png'),
			'stone_break10': load_image('tiles/stone_break10.png'),
			'water_1': load_image('tiles/water_1.png'),
			'water_2': load_image('tiles/water_2.png'),
			'water_3': load_image('tiles/water_3.png'),
			'water_4': load_image('tiles/water_4.png'),
			'water_5': load_image('tiles/water_5.png'),
			'wheat_1': load_image('tiles/wheat-1.png'),
			'wheat_2': load_image('tiles/wheat-2.png'),
			'wheat_3': load_image('tiles/wheat-3.png'),
			'wheat_4': load_image('tiles/wheat-4.png'),
			'wheat_5': load_image('tiles/wheat-5.png'),
			'wheat_6': load_image('tiles/wheat-6.png'),
			'wheat_7': load_image('tiles/wheat-7.png'),
			'wheat_8': load_image('tiles/wheat-8.png'),
			'wood_door_down': load_image('tiles/wood_door_down.png'),
			'wool_blue': load_image('tiles/wool_blue.png'),
			'wool_brown': load_image('tiles/wool_brown.png'),
			'wool_cyan': load_image('tiles/wool_cyan.png'),
			'wool_gray': load_image('tiles/wool_gray.png'),
			'wool_green': load_image('tiles/wool_green.png'),
			'wool_light_blue': load_image('tiles/wool_light_blue.png'),
			'wool_light_brown': load_image('tiles/wool_light_brown.png'),
			'wool_light_gray': load_image('tiles/wool_light_gray.png'),
			'wool_lime': load_image('tiles/wool_lime.png'),
			'wool_magenta': load_image('tiles/wool_magenta.png'),
			'wool_orange': load_image('tiles/wool_orange.png'),
			'wool_pink': load_image('tiles/wool_pink.png'),
			'wool_purple': load_image('tiles/wool_purple.png'),
			'wool_red': load_image('tiles/wool_red.png'),
			'wool_yellow': load_image('tiles/wool_yellow.png'),
		}
        self.display_surf = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.scroll = [0,0]
        self.setup()
    def setup(self):
        self.player = Player((320,100), self.all_sprites)
        self.tilemap = Tilemap(renderer=self)
        self.crosshair = Crosshair()
    def run(self,dt):
        self.scroll[0] += (self.player.rect.centerx - self.display_surf.get_width() / 2 - self.scroll[0])
        self.scroll[1] += (self.player.rect.centery - self.display_surf.get_height() / 2 - self.scroll[1])
        render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
        self.display_surf.fill('black')
        self.tilemap.render(self.display_surf, offset = render_scroll)
        self.all_sprites.update(dt,self.tilemap)
        self.player.mouse_input(self.tilemap,(self.crosshair.tile[0]*16 + render_scroll[0],self.crosshair.tile[1]*16 + render_scroll[1]))
        self.player.render(self.display_surf, offset = render_scroll)
        self.crosshair.update(pygame.mouse.get_pos(), self.display_surf, render_scroll)
        self.screen.blit(self.display_surf)