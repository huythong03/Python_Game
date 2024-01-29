import pygame

class Pipe(pygame.sprite.Sprite):
	def __init__(self, pos, width, height, flip):
		super().__init__()
		self.width = width
		img_path = 'assets/terrain/pipe.png'
		self.image = pygame.image.load(img_path)
		self.image = pygame.transform.scale(self.image, (width, height))
		if flip:
			flipped_image = pygame.transform.flip(self.image, False, True)
			self.image = flipped_image
		self.rect = self.image.get_rect(topleft = pos)

	# Cập nhật vị trí đối tượng do cuộn thế giới
	def update(self, x_shift):
		self.rect.x += x_shift

		# loại bỏ đường ống trong màn hình trò chơi khi nó không được hiển thị trên màn hình nữa
		if self.rect.right < (-self.width):
			self.kill()