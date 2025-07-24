# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

import sys

from constants import *

from player import *

from circleshape import *

from asteroid import *

from asteroidfield import *

from shot import *

def main():
    pygame.init()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)
    player = Player(x, y)

    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatables, drawables)    
    
    
    running = True
    while running:
        screen.fill(BLACK)
        updatables.update(dt)
        for obj in drawables:
            obj.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
                    break
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
