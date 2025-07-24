import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(
            x,
            y,
            radius,
        )

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position.xy, self.radius, 2)