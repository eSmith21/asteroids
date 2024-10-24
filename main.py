import pygame
from constants import *
from player import Player


def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting asteroids!")
	print("Screen width: 1280")
	print("Screen height: 720")

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))

		player.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60) / 1000





if __name__ == "__main__":
	main()
