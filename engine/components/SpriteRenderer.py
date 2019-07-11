from .BaseComponent import BaseComponent
from engine.subsystems.sprite import Sprite

class SpriteRenderer(BaseComponent):
    def init(self, img_path):
        self.sprite = Sprite(img_path)

    def update(self, screen):
        screen.blit(self.sprite.sprite, self.game_object.transform)
