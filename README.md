# pyosrs - Python Library for Old School RuneScape

pyosrs is a Python library that provides a simple interface for retrieving and parsing data from the Old School RuneScape hiscores.

## Installation

To install pyosrs, you can use pip:

```
pip install pyosrs
```

## Usage

### Retrieving Hiscores

To retrieve the hiscore for a player, you can create a Pyosrs instance and use its get_hiscore method. Here's an example:

```python
import asyncio
from pyosrs.client import Pyosrs
from pyosrs.enums import GAME_MODE

async def main():
    async with Pyosrs() as pyosrs:
        hiscore = await pyosrs.get_hiscore("username")
        # With game mode
        hiscore = await pyosrs.get_hiscore("username", GAME_MODE.MAIN)
        print(hiscore.skills.overall.rank)
        print(hiscore.skills.overall.level)
        print(hiscore.skills.overall.experience)

asyncio.run(main())
```

This will output the overall rank, level, and experience for the player in the main game mode.

### Retrieving Game Mode

To retrieve the game mode for a player, you can use `get_game_mode` method which returns a tuple of the game mode and the player's hiscore object. Here's an example:

```python
game_mode, hiscore = await pyosrs.get_game_mode("username")
```

### Handling Errors

If the username provided is invalid, a `InvalidUserException` exception will be raised. If there is a new type of hiscore data response that hasn't been accounted for, a `InvalidAPIResponseException` exception will be raised.

```python
try:
    hiscore = await pyosrs.get_hiscore("invalid username")
except InvalidUserException:
    print("Invalid username")
```

## Contributing

If you would like to contribute to pyosrs, please feel free to submit a pull request or open an issue on the GitHub repository.

Here's a quick start guide to setup the project:

```bash
git clone https://github.com/phongse/pyosrs.git
cd pyosrs

# Create virtual environment
python -m venv .venv

# Activate venv (Linux, Mac)
source .venv/bin/activate

# Activate venv (Windows)
.\venv\Scripts\Activate.ps1

# Install poetry and pyosrs dependencies
python -m pip install --upgrade pip poetry
poetry install --with dev

# Install pre-commit
pre-commit install
```

With `make` you can run tests and format the code:

```bash
make format
make mypy
make tests
make precommit
```

## License

pyosrs is licensed under the GNU Lesser General Public License. See [LICENSE](https://github.com/phongse/pyosrs/blob/main/LICENSE).
