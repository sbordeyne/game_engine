import pygame
import sys
from .subsystems.physics_engine import PhysicsEngine
from .subsystems.renderer import Renderer
from .subsystems.input import Input


class GameManager:
    def __init__(self, resolution):
        pygame.init()
        self.resolution = self.width, self.height = resolution
        self.screen = pygame.display.set_mode(self.resolution)
        self.done = False
        self.physics_engine = PhysicsEngine(self)
        self.renderer = Renderer(self)
        self.input = Input(self)
        self.game_objects = []

    def start(self):
        for go in self.game_objects:
            go.awake()
        self.loop()

    def loop(self):
        while not self.done:
            if self.input.get_quit():
                self.done = False
            # self.physics_engine.iterate(self)
            self.renderer.render()
            for go in self.game_objects:
                go.call_updates()

        sys.exit(1)
