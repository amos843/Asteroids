from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
    
    def draw(self, screen):
        # draw at the current position tracked by the base class
        pygame.draw.circle(
            screen,
            "white",
            (self.position.x, self.position.y),
            self.radius,
            LINE_WIDTH,
        )
    
    def update(self, dt):
        self.position += self.velocity * dt 