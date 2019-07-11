import env
import pygame
from engine.GameManager import GameManager
from engine.GameObject import GameObject
from engine.components.SpriteRenderer import SpriteRenderer
from engine.subsystems.input import JoyButton, KeyButton, MouseButton, Input

def player_awake(self):
    self.movespeed = 5

def player_update(self):
    if Input.get_button_down(KeyButton("left", [pygame.K_LEFT])):
        self.transform.move(self.movespeed)


game_manager = GameManager((1024, 768))
player = GameObject(game_manager, position=(10, 30))
player_spriterenderer_component = SpriteRenderer("player", game_manager, init_args={"img_path": "assets/player.png"})
player.add_component(player_spriterenderer_component)
player.update = player_update
player.awake = player_awake

game_manager.start()
