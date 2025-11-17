import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.speed = 5
    def movement(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
    def draw(self, display):
        pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, 50, 50))