import pygame
from tilemap import Tileset

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.Surface((32,64))
        self.image.fill('green')
        self.rect = self.image.get_frect(center = pos)
        self.collisions = {'up':False, 'down': False, 'left':False, 'right':False}
        self.pos = pygame.math.Vector2(self.rect.center) 
        self.acceleration = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.jump_str = -200
        self.walk_str = 150
        self.run_str = 250
        self.jump_cnt = 0

    def input(self):
        keys = pygame.key.get_pressed()
        key_once = pygame.key.get_just_pressed()
        
        if keys[pygame.K_a]:
            self.velocity.x = -self.walk_str
            if keys[pygame.K_LSHIFT]:
                self.velocity.x = -self.run_str
        elif keys[pygame.K_d]:
            self.velocity.x = self.walk_str
            if keys[pygame.K_LSHIFT]:
                self.velocity.x = self.run_str
        else:
            self.velocity.x = 0
        if key_once[pygame.K_SPACE]:
            self.velocity.y += self.jump_str
    def move(self,dt,tileset):
        self.collisions = {'up':False, 'down': False, 'left':False, 'right':False}
        self.pos.x += self.velocity.x * dt
        for rect in tileset.rects_around(self.pos):
            if self.rect.colliderect(rect) and self.rect.bottom > rect.top + 16:
                if self.velocity.x > 0:
                    self.rect.right = rect.left
                    self.collisions['right'] = True
                if self.velocity.x < 0:
                    self.rect.left = rect.right
                    self.collisions['left'] = True
                self.pos.x = self.rect.centerx
        self.pos.y += self.velocity.y * dt 
        for rect in tileset.rects_around(self.pos):
            if self.rect.colliderect(rect):
                if self.velocity.y > 0:
                    self.rect.bottom = rect.top
                    self.collisions['down'] = True
                if self.velocity.y < 0:
                    self.rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos.y = self.rect.centery
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y
        self.velocity.y = min(500, self.velocity.y + 500 * dt)
        if self.collisions['down'] or self.collisions['up']:
            self.velocity.y = 0
        
    def update(self,dt,tileset):

        self.input()
        self.move(dt,tileset)

    def render(self, surf, offset=(0, 0)):
        surf.blit(self.image, (self.pos.x - offset[0]-16, self.pos.y - offset[1]-32))