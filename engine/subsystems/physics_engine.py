class PhysicsEngine:
    def __init__(self, game_manager):
        self.game_manager = game_manager

    def iterate(self):
        for go in self.game_manager.game_objects:
            if go.has_component("Rigidbody2D"):
                go.get_component("Rigidbody2D").update()
        pass
