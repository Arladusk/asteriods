import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS, COLOR_BLACK, GAME_TITLE
from player import Player

class Game:
    def __init__(self):
        self.running = True
        self.resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    return
            self.paint_background()
            self.player.update(self.dt)
            self.player.draw(self.screen)
            self.refresh_screen()
            self.dt = self.clock.tick(FPS) / 1000


    def paint_background(self):
        self.screen.fill(COLOR_BLACK)

    def refresh_screen(self):
        pygame.display.flip()

# Initiates pygame, creates and starts the game object. 
def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game = Game()
    game.run()

if __name__ == "__main__":
    main()