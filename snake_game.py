import pygame
import random
import tkinter as tk
from tkinter import messagebox

SNAKE_WIDTH = 10
SNAKE_HEIGHT = 10
RESOLUTION = (400, 400)

WHITE = (255, 255, 255)
BLUE = (0, 190, 190)
RED = (255, 0, 0)


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


class Snake():
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"

    def change_direction_to(self, dir):
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"

        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"

        if dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"

        if dir == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def update(self):
        if self.direction == "RIGHT":
            if self.position[0] <= RESOLUTION[0] - SNAKE_WIDTH:
                self.position[0] += 10
            else:
                self.position[0] = 0

        if self.direction == "LEFT":
            if self.position[0] >= 10:
                self.position[0] -= 10
            else:
                self.position[0] = RESOLUTION[0] - SNAKE_WIDTH

        if self.direction == "UP":
            if self.position[1] >= 10:
                self.position[1] -= 10
            else:
                self.position[1] = RESOLUTION[0] - SNAKE_WIDTH

        if self.direction == "DOWN":
            if self.position[1] <= RESOLUTION[0] - 2 * SNAKE_WIDTH:
                self.position[1] += 10
            else:
                self.position[1] = 0

    def move(self, foodpos):
        self.body.insert(0, list(self.position))
        if self.position == foodpos:
            return 1
        else:
            self.body.pop()
            return 0

    def check_collision(self):
        if self.position in self.body[1:]:
            return 1
        return 0


class Food():
    def __init__(self):
        self.position = [random.randrange(1, RESOLUTION[0]/10) * 10, random.randrange(1, RESOLUTION[1]/10) * 10]

    def generate(self, snake_Body):
        while True:
            self.position = [random.randrange(1, RESOLUTION[0]/10) * 10, random.randrange(1, RESOLUTION[1]/10) * 10]
            if self.position not in snake_Body:
                break
        return self.position

    def draw(self):
        pygame.draw.rect(win, RED, (self.position[0], self.position[1], SNAKE_WIDTH, SNAKE_HEIGHT))


if __name__ == "__main__":
    pygame.init()
    score = 0
    win = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption("SNAKE GAME      SCORE = " + str(score))
    velocity = 10
    snake = Snake()
    food = Food()
    run = True
    while run:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.change_direction_to("RIGHT")
                if event.key == pygame.K_UP:
                    snake.change_direction_to("UP")
                if event.key == pygame.K_DOWN:
                    snake.change_direction_to("DOWN")
                if event.key == pygame.K_LEFT:
                    snake.change_direction_to("LEFT")

        snake.update()
        snake.move(food.position)
        if (snake.position == food.position):
            score += 1
            velocity += 1
            pygame.display.set_caption("SNAKE GAME      SCORE = " + str(score))
            food.generate(snake.body)

        win.fill(BLUE)
        if snake.check_collision() == 1:
            message_box('You Lost!', "You bit yourself \n GAME OVER")
            run = False

        for part in snake.body:
            pygame.draw.rect(win, WHITE, (part[0], part[1], SNAKE_WIDTH, SNAKE_HEIGHT))
        food.draw()

        pygame.display.flip()
    pygame.quit()
