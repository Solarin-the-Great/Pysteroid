import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(
            x,
            y,
            radius,
        )

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position.xy, self.radius, 2)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        self.kill()
        
        random_angle = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid.velocity = new_velocity_1 * 1.2

        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = new_velocity_2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt