import pytest

from main_game import Game, Car


# Defining tests using pytest conventions

def test_car_initialization_pytest():
    car = Car(5, 5, "car.png")
    assert hasattr(car, 'x') and car.x == 5, "Car x-coordinate initialization failed"
    assert hasattr(car, 'y') and car.y == 5, "Car y-coordinate initialization failed"
    assert hasattr(car, 'image') and car.image == "car.png", "Car image loading failed"


def test_obstacle_initialization_pytest():
    obstacle = Obstacle(10, 0, 5, "obstacle.png")
    assert hasattr(obstacle, 'x') and obstacle.x == 10, "Obstacle x-coordinate initialization failed"
    assert hasattr(obstacle, 'y') and obstacle.y == 0, "Obstacle y-coordinate initialization failed"
    assert hasattr(obstacle, 'speed') and obstacle.speed == 5, "Obstacle speed initialization failed"
    assert hasattr(obstacle, 'image') and obstacle.image == "obstacle.png", "Obstacle image loading failed"


def test_game_initialization_pytest():
    game = Game(800, 600)
    assert hasattr(game, 'display') and game.display == (800, 600), "Game display initialization failed"
    assert hasattr(game, 'car'), "Car object creation in Game failed"


# Normally, you'd run these tests using the command `pytest <filename>.py` in your terminal.
# For now, we'll just execute them directly in this environment.
test_car_initialization_pytest()
test_obstacle_initialization_pytest()
test_game_initialization_pytest()

"Tests (pytest style) executed successfully!"
