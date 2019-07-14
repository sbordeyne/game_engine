from .BaseComponent import BaseComponent
from engine.utils.Vector2 import Vector2

class Rigidbody2D(BaseComponent):
    def init(self):
        self.gravity_scale = 1.0
        self.friction_coeff = 1.0
        self.forces_to_apply = []

    @property
    def center_mass(self):
        return Vector2(0, 0)

    def update(self):
        x, y = self.game_object.transform.x, self.game_object.transform.y
        y -= self.gravity_scale * 9.81
        pos = Vector2(x, y)
        for force in self.forces_to_apply:
            pos += force
        pos -= Vector2(self.friction_coeff, self.friction_coeff)
        self.game_object.transform.x, self.game_object.transform.y = pos.tuple
