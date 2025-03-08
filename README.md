# Asteroids

A simple 2D game inspired by the classic Asteroids game. In this game, you control a spaceship that must dodge and shoot asteroids.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Game](#running-the-game)
- [Controls](#controls)
- [Project Structure](#project-structure)
- [Credits](#credits)

## Requirements

- Python 3.7+ (Python 3.10+ recommended)
- Pygame 2.6.1
- A supported operating system (Windows, macOS, Linux)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Dscraft07/asteroids.git
   cd asteroids

2. **Create and activate a virtual environment (recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On macOS/Linux

- or

   ```bash
   venv\Scripts\activate      # On Windows

3. **Install the required dependencies**

   ```bash
   pip install -r requirements.txt

## Running The Game

- To start the game, run:

   ```bash
   python main.py

- You should see a window with a black background, a triangular spaceship at the center, and asteroids appearing on the screen.

## Controls

- W: Move forward
- S: Move backward
- A: Rotate left
- D: Rotate right
- Spacebar: Shoot

## Project Structure

- ├── asteroid.py       # Asteroid class (includes the split() method)
- ├── asteroidfield.py  # Manages asteroid spawning
- ├── circleshape.py    # Base class for circular game objects (inherits from pygame.sprite.Sprite)
- ├── constants.py      # Contains game constants (screen dimensions, speeds, cooldowns, etc.)
- ├── main.py           # Main game loop
- ├── player.py         # Player class (controls the spaceship, movement, and shooting)
- ├── requirements.txt  # List of dependencies (primarily pygame)
- ├── shot.py           # Shot class for bullets
- └── README.md         # This documentation file

## Credits

@Dscraft07
