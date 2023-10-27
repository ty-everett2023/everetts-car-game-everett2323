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
        self.font = pg.font.Font(None,32)
        self.text_surf = self.font.render(self.text,True,(255,255,255))

    def draw(self):
        pg.draw.rect(self.screen.screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 6)

    def is_hover(self, x, y):
        return pg.Rect(self.x, self.y, self.width, self.height).collidepoint(x, y)

    def activate(self):
        pg.draw.rect(self.screen.screen, (155, 0, 0), (self.x, self.y, self.width, self.height), 6)


class Car:
    def __init__(self, screen, image_path, x, y):
        # TODO: Initialize the x, y coordinates and load the image for the car.
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pg.image.load(image_path)

    def blit(self):
        self.screen.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, x, y, speed, image):
        # TODO: Initialize the x, y coordinates, speed, and load the image for the obstacle.
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image

    def draw(self, display):
        display.blit(self.image,(self.x, self.y))


    def move(self):
        # TODO: Move the obstacle downwards by updating the y coordinate.
        self.y += self.speed
    def has_collision(self,car):
        pg.Rect(self.x, self.y,self.image.get_width(),self.image.get_height()).colliderect(pg.Rect(car.x, car.y,car.image.get_width(),car.image.get_height()))


class Game:
    def __init__(self):
        # TODO: Initialize pygame, set the display mode, and create a Car object.
        pg.init()
        pg.mixer.init()
        self.screen = Screen(798, 600)
        self.everetts_car = Car(self.screen, '/Users/chrisloxley/everetts-car-game-everett2323/Assets/car.png', 350,
                                495)
        self.enemy_cars = [
            Car(self.screen, '/Users/chrisloxley/everetts-car-game-everett2323/Assets/car1.jpeg',
                random.randint(178, 490), 100),
            Car(self.screen, '/Users/chrisloxley/everetts-car-game-everett2323/Assets/car2.png',
                random.randint(178, 490), 100),
            Car(self.screen, '/Users/chrisloxley/everetts-car-game-everett2323/Assets/car3.png',
                random.randint(178, 490), 100)
        ]
        self.obstacles = []
        font_name = pg.font.match_font('arial')
        self.intro_font = pg.font.Font(font_name, 38)
        self.play_button = Button(self.screen, 60, 440, 175, 50, "Play")
        self.instruction_button = Button(self.screen, 265, 440, 300, 50, "Instructions")
        self.about_button = Button(self.screen, 600, 440, 165, 50, "About")

    def intro_img(self, x, y):
        intro = pg.image.load("/Users/chrisloxley/everetts-car-game-everett2323/Assets/intro.png")
        self.screen.blit(intro, (x, y))

    def about_img(self, x, y):
        about = pg.image.load("/Users/chrisloxley/everetts-car-game-everett2323/Assets/About.png")
        self.screen.blit(about, (x, y))

    def intro_screen(self):
        run = True
        while run:
            self.screen.fill((0, 0, 0))
            self.intro_img(0, 0)
            self.play_button.draw()
            self.instruction_button.draw()
            self.about_button.draw()

            x, y = pg.mouse.get_pos()
            click = False

            if self.play_button.is_hover(x, y):
                self.play_button.activate()
                if click:
                    self.countdown()

            if self.instruction_button.is_hover(x, y):
                self.instruction_button.activate()
                if click:
                    self.intro_img(0, 0)

            if self.about_button.is_hover(x, y):
                self.about_button.activate()
                if click:
                    self.about_img(0, 0)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            self.screen.update()



    def spawn_obstacle(self):
        # TODO: Generate an obstacle with random x position and add it to the obstacles list.
        enemy_car = random.choice(self.enemy_cars)
        obstacle = Obstacle(enemy_car.x, enemy_car.y,5,enemy_car.image)
        self.obstacles.append(obstacle)

    def run(self):
        # TODO: Start the game loop, handle events, move the car and obstacles, and check for collisions.
        self.intro_screen()
        run = True
        while run:
            self.screen.fill((0,0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            self.screen.update()


if __name__ == '__main__':
    # TODO: Create a Game object and start the game by calling the run method.
    game = Game()
    game.run()
