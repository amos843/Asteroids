import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    #initialize pygame
    pygame.init()
    
    #create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #groups to manage objects
    updatable = pygame.sprite.Group() #all objects that can be updated
    drawable = pygame.sprite.Group() #all objects that can be drawn

    #add player class to both groups
    Player.containers = (updatable, drawable)

    #create the player object
    p1 = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)

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
        
        #fill screen with a solid black color
        screen.fill("black")
  
        #draw the player object (white triangle)
        for thing in drawable:
            thing.draw(screen)

        #update player movement
        updatable.update(dt)

        #pygame function to refresh screen to update to gamestate
        pygame.display.flip()
        
        #update dt
        dt = clock.tick(60) / 1000

    #print("Starting Asteroids with pygame version:", pygame.__version__)
    #print("Screen width:", SCREEN_WIDTH)
    #print("Screen height:", SCREEN_HEIGHT)

    

if __name__ == "__main__":
    main()
