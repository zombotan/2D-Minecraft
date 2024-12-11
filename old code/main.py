import pygame
import sys
from settings import *
from render import Renderer

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1280, 720))
		pygame.display.set_caption('2D Minecraft')
		self.display = pygame.display.get_surface()
		self.renderer = Renderer(self.screen)
		self.clock = pygame.time.Clock()
		self.font = pygame.font.SysFont('Monocraft', 16, bold=False, italic=False)
	def run(self):
		while True:
			dt = self.clock.tick() / 1000
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			self.renderer.run(dt)
			self.fps_counter()
			pygame.display.update()
	def fps_counter(self):
		fps = str(int(self.clock.get_fps()))
		fps_t = self.font.render(fps , 1, pygame.Color("RED"))
		self.display.blit(fps_t,(0,0))
Game().run()