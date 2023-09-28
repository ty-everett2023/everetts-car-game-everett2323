import pygame
import random
import sys


class Car:
    def __init__(self, x, y, image):
        # TODO: Initialize the x, y coordinates and load the image for the car.
        pass

    def draw(self, display):
        # TODO: Draw the car on the display at the x, y coordinates.
        pass

    def move(self, x_change, y_change):
        # TODO: Update the x, y coordinates of the car.
        pass


class Obstacle:
    def __init__(self, x, y, speed, image):
        # TODO: Initialize the x, y coordinates, speed, and load the image for the obstacle.
        pass

    def draw(self, display):
        # TODO: Draw the obstacle on the display at the x, y coordinates.
        pass

    def move(self):
        # TODO: Move the obstacle downwards by updating the y coordinate.
        pass


class Game:
    def __init__(self, display_width, display_height):
        # TODO: Initialize pygame, set the display mode, and create a Car object.
        pass

    def spawn_obstacle(self):
        # TODO: Generate an obstacle with random x position and add it to the obstacles list.
        pass

    def run(self):
        # TODO: Start the game loop, handle events, move the car and obstacles, and check for collisions.
        pass


if __name__ == '__main__':
    # TODO: Create a Game object and start the game by calling the run method.
    pass
