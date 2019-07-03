class BaseComponent:
    def __init__(self, name, game_manager, init_args={}):
        self.name = name
        self.game_object = None
        self.game_manager = game_manager
        self.type = type(self).__name__
        self.init(**init_args)

    def init(self, **kwargs):
        pass

    def update(self):
        pass
