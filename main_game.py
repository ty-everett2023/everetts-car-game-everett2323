import pygame as pg
import random
import sys


class Screen:
    def __init__(self, width, height):
        self.screen = pg.display.set_mode((width, height))
        self.width = width
        self.height = height
        pg.display.set_caption("Everett's derby")
        logo = pg.image.load('/Users/chrisloxley/everetts-car-game-everett2323/Assets/logo.jpeg')
        pg.display.set_icon(logo)

    def fill(self, color):
        self.screen.fill(color)

    def blit(self, image, coordinates):
        self.screen.blit(image, coordinates)

    def update(self):
        pg.display.update()

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

class Button:
    def __init__(self, screen, x, y, width, height, text):
        self.text = text
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pg.font.Font(None, 32)
        self.text_surf = self.font.render(self.text, True, (255, 255, 255))

    def draw(self):
        pg.draw.rect(self.screen.screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 6)
        text_x = self.x + (self.width - self.text_surf.get_width()) // 2
        text_y = self.y + (self.height - self.text_surf.get_height()) // 2
        self.screen.screen.blit(self.text_surf, (text_x, text_y))

    def is_hover(self, x, y):
        return pg.Rect(self.x, self.y, self.width, self.height).collidepoint(x, y)

    def activate(self):
        pg.draw.rect(self.screen.screen, (155, 0, 0), (self.x, self.y, self.width, self.height), 6)


class Car(pg.sprite.Sprite):
    def __init__(self, screen, image_path, x, y):
        # TODO: Initialize the x, y coordinates and load the image for the car.
        super().__init__()
        original_img = pg.image.load(image_path).convert_alpha()
        self.screen = screen
        self.image = pg.transform.rotate(original_img, -90)
        self.rect = self.image.get_rect(center=(x,y))
        self.speed = 200
        self.velocity = pg.math.Vector2(0,0)
        self.acceleration = .5
    def update(self, delta_time, move_left, move_right):
        if move_left:
            self.velocity.x = max(self.velocity.x - self.acceleration, -self.speed)
        elif move_right:
            self.velocity.x = max(self.velocity.x + self.acceleration, self.speed)
        else:
            self.velocity.x *= .9
        if abs(self.velocity.x)<1 and (move_left or move_right):
            self.velocity.x = -self.speed if move_left else self.speed
        self.rect.x += self.velocity.x * delta_time
        self.rect.clamp_ip(self.screen.screen.get_rect())
    def blit(self):
        self.screen.screen.blit(self.image, self.rect.topleft)


class Obstacle:
    def __init__(self,screen, image, x, y ):
        # TODO: Initialize the x, y coordinates, speed, and load the image for the obstacle.
        self.screen = screen
        self.image = pg.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 100

    def update(self, delta_time):
        self.rect.y += self.speed * delta_time

    def blit(self):
        self.screen.screen.blit(self.image, self.rect.topleft)

    def has_collision(self, car_rect):
        return self.rect.colliderect(car_rect)


class Game:
    def __init__(self):
        # TODO: Initialize pygame, set the display mode, and create a Car object.
        pg.init()
        pg.mixer.init()
        self.screen = Screen(798, 600)
        self.everetts_car = Car(self.screen, 'Assets/car.png', 350,
                                495)
        self.enemy_cars = [
            Car(self.screen, 'Assets/car1.jpeg',
                random.randint(178, 490), 100),
            Car(self.screen, 'Assets/car2.png',
                random.randint(178, 490), 100),
            Car(self.screen, 'Assets/car3.png',
                random.randint(178, 490), 100)
        ]
        self.obstacles = []
        font_name = pg.font.match_font('arial')
        self.intro_font = pg.font.Font(font_name, 38)
        self.play_button = Button(self.screen, 60, 440, 175, 50, "Play")
        self.instruction_button = Button(self.screen, 265, 440, 300, 50, "Instructions")
        self.about_button = Button(self.screen, 600, 440, 165, 50, "About")
        self.city_1 = pg.image.load("Assets/city_1.png")
        self.city_2 = pg.image.load("Assets/city_2.png")
        self.city_3 = pg.image.load("Assets/city_3.png")
        self.current_city = self.city_1
        self.everetts_car.x = (self.screen.get_width() / 2) - (self.everetts_car.image.get_width() / 2)

    def countdown(self):
        font = pg.font.Font(None, 72)
        count_nums = [3, 2, 1]
        for counter in count_nums:
            self.screen.fill((0, 0, 0))
            num_surface = font.render(str(counter), True, (255, 255, 255))
            num_rect = num_surface.get_rect(
                center=(self.screen.screen.get_width() / 2, self.screen.screen.get_height() / 2))
            self.screen.screen.blit(num_surface, num_rect.topleft)
            self.screen.update()
            pg.time.delay(1000)
        self.run()

    def intro_img(self, x, y):
        intro = pg.image.load("Assets/intro.png")
        self.screen.blit(intro, (x, y))

    def about_img(self, x, y):
        about = pg.image.load("Assets/About.png")
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

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run=False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

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
            pg.display.flip()

    def spawn_obstacle(self):
        # TODO: Generate an obstacle with random x position and add it to the obstacles list.
        obstacle_x = random.randint(178, 490)
        obstacle_image = random.choice(["Assets/car1.jpeg", "Assets/car2.png", "Assets/car2.png"])
        obstacle = Obstacle(self.screen, obstacle_image, obstacle_x, -100)
        self.obstacles.append(obstacle)

    def run(self):
        # TODO: Start the game loop, handle events, move the car and obstacles, and check for collisions.
        clock = pg.time.Clock()
        move_left = False
        move_right = False
        run = True
        while run:
            delta_time = clock.tick(60) / 1000.0
            self.screen.fill((0,0,0))
            self.screen.blit(self.current_city, (0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        move_left = True
                    elif event.key == pg.K_RIGHT:
                        move_right = True
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT:
                        move_left = False
                    if event.key == pg.K_RIGHT:
                        move_right = False
            self.everetts_car.update(delta_time, move_left, move_right)
            self.everetts_car.blit()
            for obstacle in self.obstacles:
                obstacle.update(delta_time)
                obstacle.blit()
            pg.display.flip()

if __name__ == '__main__':
    # TODO: Create a Game object and start the game by calling the run method.
    game = Game()
    game.intro_screen()
