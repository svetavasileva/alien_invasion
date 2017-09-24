import pygame
import sys
from random import randint

pygame.init()
screen = pygame.display.set_mode((1000,800))
image = pygame.image.load('images/star.bpm')
img = pygame.transform.scale(image, (60, 60))
rect = img.get_rect()
random_number = randint(0,800)
rect.x = random_number
rect.y = random_number
screen.fill((90, 80, 200))
screen.blit(img,rect)

while True:
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()