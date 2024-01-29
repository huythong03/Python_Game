import pygame
from settings import import_sprite

class Bird(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		# Thông tin cơ bản về chim
		self.frame_index = 0
		self.animation_delay = 3
		self.jump_move = -9

		# Hoạt hình chim
		self.bird_img = import_sprite("assets/bird")
		self.image = self.bird_img[self.frame_index]
		self.image = pygame.transform.scale(self.image, (size, size))
		self.rect = self.image.get_rect(topleft = pos)
		self.mask = pygame.mask.from_surface(self.image)

		# tình trạng chim
		self.direction = pygame.math.Vector2(0, 0)
		self.score = 0

	# cho hoạt hình bay của chim
	def _animate(self):
		sprites = self.bird_img
		sprite_index = (self.frame_index // self.animation_delay) % len(sprites)
		self.image = sprites[sprite_index]
		self.frame_index += 1
		self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
		self.mask = pygame.mask.from_surface(self.image)
		if self.frame_index // self.animation_delay > len(sprites):
			self.frame_index = 0

	# để chim bay cao hơn
	def _jump(self):
		self.direction.y = self.jump_move

	# cập nhật trạng thái tổng thể của chim
	def update(self, is_jump):
		if is_jump:
			self._jump()
		self._animate()