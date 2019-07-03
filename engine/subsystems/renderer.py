class Renderer:
    def __init__(self, gm):
        self.game_manager = gm

    def render(self):
        self.game_manager.screen.fill((0, 0, 0))
        for go in self.game_manager.game_objects:
            sprite_renderer = go.get_component("SpriteRenderer")
            if sprite_renderer:
                sprite_renderer.update(self.game_manager.screen)
