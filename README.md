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
import engine
from engine.components.SpriteRenderer import SpriteRenderer
from engine.subsystems.input import JoyButton, KeyButton, MouseButton, Input

def player_awake(self):
    self.movespeed = 5

def player_update(self):
    if Input.get_button_down(KeyButton("left", [pygame.K_LEFT])):
        self.transform.move(self.movespeed)


game_manager = engine.GameManager.GameManager()
player = engine.GameObject.GameObject(game_manager, position=(10, 30))
player_spriterenderer_component = SpriteRenderer("player", game_manager, init_args={"img_path": "assets/player.png"})
player.add_component(player_spriterenderer_component)
player.update = player_update
player.awake = player_awake

game_manager.start()

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
