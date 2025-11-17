import pygame
from player import Player

class Game:
    def __init__(self):
        pygame.init()
    def main(self):
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygame Thingy")
        clock = pygame.time.Clock()
        run = True
        p1 = Player(350, 250)
        while run:
            screen.fill((0, 255, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            p1.movement(keys=pygame.key.get_pressed())
            p1.draw(display=screen)
            clock.tick(60)
            pygame.display.flip()
        pygame.quit()
Game().main()