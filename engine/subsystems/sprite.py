import pygame


class Sprite:
    def __init__(self, img_path):
        self.img_path = img_path
        self.sprite = pygame.image.load(img_path)
