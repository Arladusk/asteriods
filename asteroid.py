import pygame
import random
from circleshape import CircleShape
from constants import COLOR_WHITE, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.width = 2

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_WHITE, self.position, self.radius, self.width)

    def update(self, dt):
          self.position += self.velocity * dt

    def split(self):
        velocity = self.velocity
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle =  random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_velocity_one = self.velocity.rotate(angle) * 1.2
            new_velocity_two = self.velocity.rotate(-angle) * 1.2
            self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_one.velocity = new_velocity_one
            asteroid_two.velocity = new_velocity_two