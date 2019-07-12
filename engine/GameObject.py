import pygame
from .exceptions import EngineException
from .components.BaseComponent import BaseComponent


class GameObject:
    def __init__(self, game_manager, position=(0, 0)):
        self.transform = self._rect = pygame.Rect(position, (0, 0))
        self.components = []
        self.game_manager = game_manager
        self.game_manager.game_objects.append(self)
        pass

    def call_updates(self):
        if self.has_component("SpriteRenderer"):
            self.transform = self._rect = self.get_component("SpriteRenderer").sprite.sprite.get_rect()
        for component in self.components:
            component.update(self.game_manager.screen)
        self.update()
        self.late_update()

    def add_component(self, component):
        if not isinstance(component, BaseComponent):
            raise EngineException("Type mismatch : component to add is not an instance of BaseComponent")
        if component.type not in [c.type for c in self.components]:
            component.game_object = self
            self.components.append(component)
        else:
            raise EngineException("Tried to add a component to a game object that has the same component type.")

    def get_component(self, component_type):
        if component_type in [c.type for c in self.components]:
            return [c for c in self.components if c.type == component_type][0]
        else:
            return False

    def has_component(self, component_type):
        return component_type in [c.type for c in self.components]

    def awake(self, *args):
        pass

    def update(self, *args):
        pass

    def fixed_update(self, *args):
        pass

    def late_update(self, *args):
        pass
