import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape
from constants import COLOR_PINK

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_PINK, self.position, SHOT_RADIUS)

    def update(self, dt):
          self.position += self.velocity * dt