import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color="black")
        for item in drawable:
            item.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision(asteroid):
                    asteroid.split()
                    bullet.kill()
        for asteroid in asteroids:
            if asteroid.collision(player):
                sys.exit("Game over!")
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()