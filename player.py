import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_frect()
        self.collisions = {'up':False, 'down': False, 'left':False, 'right':False}
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
        self.rect.centerx += self.velocity.x * dt
        for rect in tileset.rects_around(self.rect.center):
            if self.rect.colliderect(rect):
                if self.velocity.x > 0:
                    self.rect.right = rect.left
                    self.collisions['right'] = True
                if self.velocity.x < 0:
                    self.rect.left = rect.right
                    self.collisions['left'] = True
        self.rect.centery += self.velocity.y * dt 
        for rect in tileset.rects_around(self.rect.center):
            if self.rect.colliderect(rect) and (self.rect.bottom > rect.top or self.rect.top < rect.bottom):
                if self.velocity.y > 0:
                    self.rect.bottom = rect.top
                    self.collisions['down'] = True
                if self.velocity.y < 0:
                    self.rect.top = rect.bottom
                    self.collisions['up'] = True
        self.velocity.y = min(2400, self.velocity.y + 600 * dt)
        if self.collisions['down'] or self.collisions['up']:
            self.velocity.y = 0
        if self.collisions['left'] or self.collisions['right']:
            self.velocity.x = 0
        
    def mouse_input(self,tileset,pos):
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            tileset.break_block(pos)
                        
    def update(self,dt,tileset):
        self.input()
        self.move(dt,tileset)

    def render(self, surf, offset=(0, 0)):
        surf.blit(self.image, (self.rect.left - offset[0], self.rect.top - offset[1]))