from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
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

    def split(self):
        self.kill()
        
        #destroy small asteroids
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        #Angle to generate new asteroids
        genangle = random.uniform(20, 50)

        #calculate new asteroids vectors
        newvector1 = self.velocity.rotate(genangle)
        newvector2 = self.velocity.rotate(0-genangle)

        newradius = self.radius - ASTEROID_MIN_RADIUS

        newasteroid1 = Asteroid(self.position.x, self.position.y, newradius)
        newasteroid2 = Asteroid(self.position.x, self.position.y, newradius)

        newasteroid1.velocity = newvector1 * 1.2
        newasteroid2.velocity = newvector2 * 1.2