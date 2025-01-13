import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS

def fill_screen(screen: pygame.Surface):
    black = (0, 0, 0)
    screen.fill(black) 

def main_loop(screen: pygame.Surface):
        while True:
            fill_screen(screen)
            pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    main_loop(screen)

if __name__ == "__main__":
    main()