import pygame as pg
import random
import sys


class Screen:
    def __init__(self, width, height):
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption("Everett's derby")
        logo = pg.image.load('/Users/chrisloxley/everetts-car-game-everett2323/Assets/logo.jpeg')
        pg.display.set_icon(logo)

    def fill(self, color):
        self.screen.fill(color)

    def blit(self, image, coordinates):
        self.screen.blit(image, coordinates)

    def update(self):
        pg.display.update()


class Button:
    def __init__(self, screen, x, y, width, height, text):
        self.text = text
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pg.draw.rect(self.screen.screen,(255,255,255),(self.x,self.y,self.width,self.height),6)
    def is_hover(self,x,y):
        return pg.Rect(self.x,self.y,self.width,self.height).collidepoint(x,y)
    def activate(self):
        pg.draw.rect(self.screen.screen,(155,0,0),(self.x,self.y,self.width,self.height),6)




class Car:
    def __init__(self, x, y, image):
        # TODO: Initialize the x, y coordinates and load the image for the car.
        self.x = x
        self.y = y
        pg.image.load(image)

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
