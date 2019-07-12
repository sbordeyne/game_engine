# GameEngine

GameEngine is a Python library to abstract pygame boilerplate code. Inspired by the UnityEngine component system.

## Installation

Once this is uploaded to PyPI, use the package manager [pip](https://pip.pypa.io/en/stable/) to install GameEngine.

```bash
pip install game_engine
```

In the meantime, you can just clone this repository, and place the engine folder in whatever project you want to work on.

## Usage

```python
import pygame
from engine import GameManager
from engine import GameObject
from engine.components.SpriteRenderer import SpriteRenderer
from engine.subsystems.input import JoyButton, KeyButton, MouseButton, Input
from engine.util.Vector2 import Vector2


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

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
