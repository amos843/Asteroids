import pygame
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape

def main():
    #initialize pygame
    pygame.init()
    
    #create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #groups to manage objects
    updatable = pygame.sprite.Group() #all objects that can be updated
    drawable = pygame.sprite.Group() #all objects that can be drawn
    asteroids = pygame.sprite.Group() #all the Asteroids

    #add player class to both groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    #create the player object
    p1 = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)

    #asteroid field object
    a1 = AsteroidField()

    #FPS control
    clock = pygame.time.Clock()
    dt = 0

    #game loop
    while(True):
        
        #sends pictures of the gamestate to jsonl file for boot.dev review
        log_state()
        
        #checks if the user closed GUI, if so, closes program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #update all game objects before drawing so we render their latest state
        updatable.update(dt)

        #check for player collision with asteroids
        for items in asteroids:
            if items.collides_with(p1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        #fill screen and draw all drawable sprites
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)

        #pygame function to refresh screen to update to gamestate
        pygame.display.flip()
        
        #update dt
        dt = clock.tick(60) / 1000

    #print("Starting Asteroids with pygame version:", pygame.__version__)
    #print("Screen width:", SCREEN_WIDTH)
    #print("Screen height:", SCREEN_HEIGHT)

    

if __name__ == "__main__":
    main()
