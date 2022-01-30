from turtle import width
import pygame

class Bat(pygame.sprite.Sprite):
    def __init__(self, screen_width, wasd = True):
        super().__init__()
        self.image = pygame.Surface((25, 300))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (50, 500)
        self.screen_width = screen_width
        self.wasd = wasd
    
    def limit_x(self):
        if self.rect.center[0] > self.screen_width/2:
            self.rect.x = self.screen_width/2 - 1

    def update(self):
        key = pygame.key.get_pressed()
        if self.wasd:
            if key[pygame.K_a]:
                self.rect.move_ip(-20, 0)
            if key[pygame.K_d]:
                self.rect.move_ip(20, 0)
            if key[pygame.K_w]:
                self.rect.move_ip(0, -20)
            if key[pygame.K_s]:
                self.rect.move_ip(0, 20)
        else:
            if key[pygame.K_LEFT]:
                self.rect.move_ip(-20, 0)
            if key[pygame.K_RIGHT]:
                self.rect.move_ip(20, 0)
            if key[pygame.K_UP]:
                self.rect.move_ip(0, -20)
            if key[pygame.K_DOWN]:
                self.rect.move_ip(0, 20)
        self.limit_x()
        
    