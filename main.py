import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting asteroids!")
	print("Screen width: 1280")
	print("Screen height: 720")

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	Shot.containers = (updatable, drawable, shots)

	asteroid_field = AsteroidField()

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		for sprite in updatable:
			sprite.update(dt)

		screen.fill((0, 0, 0))

		for sprite in drawable:
			sprite.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60) / 1000

		for asteroid in asteroids:
			if asteroid.is_colliding(player):
				print ("Game Over!")
				sys.exit(0)



if __name__ == "__main__":
	main()
