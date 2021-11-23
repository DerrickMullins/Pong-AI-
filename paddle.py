import pygame
BLACK = (0,0,0)

# Create paddle class that inherits from Sprite
class Paddle(pygame.sprite.Sprite):
	
	# Constructor
	def __init__(self, color, width, height):
		
		super().__init__()
		# Pass in width/height and color
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)

		# Draw the paddle rect(surface, color, rect)
		pygame.draw.rect(self.image, color, [0, 0, width, height])

		# Fetch the rect obj that has the dimensions of the image
		self.rect = self.image.get_rect()

	def moveUp(self, pixels):
		self.rect.y -= pixels
		# Make sure you arent going off the screen
		if self.rect.y < 0:
			self.rect.y = 0

	def moveDown(self, pixels):
		self.rect.y += pixels
		# Make sure you arent going off the screen
		if self.rect.y > 400:
			self.rect.y = 400