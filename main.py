import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS, COLOR_BLACK, GAME_TITLE

class Game:
    def __init__(self):
        self.running = True
        self.resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.dt = 0





# Fills the game window with Black color. 
def fill_screen(screen: pygame.Surface):
    black = (0, 0, 0)
    screen.fill(black) 

# To be written
def main_loop(screen: pygame.Surface, clock: pygame.time.Clock):
        dt = 0
        while True:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    return
            fill_screen(screen)
            pygame.display.flip()
            dt = clock.tick(60) / 1000

# Initiates pygame, creates a Display and Clock object, prints some terminal text, starts the game. 
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    main_loop(screen, clock)

if __name__ == "__main__":
    main()