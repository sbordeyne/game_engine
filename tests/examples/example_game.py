import env
import pygame
from engine import GameManager
from engine import GameObject
from engine.components.SpriteRenderer import SpriteRenderer
from engine.subsystems.input import JoyButton, KeyButton, MouseButton, Input
from engine.utils import Vector2


class Player(GameObject):
    def awake(self):
        self.movespeed = 5
        self.add_component(SpriteRenderer("player", game_manager, init_args={"img_path": "assets/player.png"}))

    def update(self):
        movement = Vector2.zero()
        if Input.get_button_down(KeyButton("left", [pygame.K_LEFT])):
            movement -= Vector2(self.movespeed, 0)
        elif Input.get_button_down(KeyButton("right", [pygame.K_RIGHT])):
            movement += Vector2(self.movespeed, 0)

        self.transform.move(*movement.tuple)


game_manager = GameManager((1024, 768))
player = Player(game_manager, position=(10, 30))
game_manager.start()
