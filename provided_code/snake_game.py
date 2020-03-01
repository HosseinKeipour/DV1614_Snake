"""
This module contains the class SnakeGame, a game-logic class for the game Snake.
"""

from random import randrange

import pygame

from .window import Window

from student_code.snake_class import Snake
from student_code.snake_class import Snake

class SnakeGame:
    """
    A simple structure for a Snake-like game.

    Attributes:
    -----------------
        window : Window
            The main window of the game.
            Makes sure that the implementation is visible to the user.

        snake_size : tuple(int, int)
            The size of the snake.

        snake : Snake
            The controllable snake.

        current_movement : Callable
            One of the four directional functions from the Snake class.
            Saved for convenience and used to call movement on the snake-attribute.

        fruit_coordinates : list(int, int)
            The positional coordinates of the fruit that the snake is to eat.

        fruit_size : tuple(int, int)
            The size of the fruit.

        running : bool
            Used to control the state of the game.
            If false, the player has either exited or lost the game.

        last_update_time : int
            If the difference between this and a clock check is above 150
            the method update_movement is called and this attribute
            updated.

    Methods:
    -----------------
        handle_keydown(event):
            Function to handle user input events incoming from the underlying pygame module.

        draw():
            Draw the game to the screen.

        move_fruit():
            Randomly moves the fruit until it does not collide with the snake anymore.
            Used after the fruit is picked up.

        fruit_pickup():
            Used to control if the snake is able to pick up the fruit.
            If the snake is able to pick the fruit up, the snake will grow
            and the fruit will be moved to a new position.

        check_if_inside_window():
            Used to control whether the snake is inside the boundaries of
            the screen or not. If the snake is not inside the boundaries,
            the game is over.

        run_game_logic():
            The main function used to run the game logic.
            Makes sure that all other functions are called as they should.

        game_loop():
            The entry point of the game.
            Clears the screen, runs the game logic, and make sure that the
            screen is presented at the end.

        update_move():
        Function to update the movement and control if the
        snake collides with itself.
    """
    #pylint: disable=no-member

    def __init__(self, background_colour, width, height):
        """Initialize the game. The parameters are passed on to the init function of Window


        Parameters:
        ------------------------------------------
        colour : list(int, int, int)
            A triple of values between 0 and 255 indicating the r, g, b value of the rectangle

        top_left : tuple(int, int)
            The x- and y-coordinates for the top left corner of the rectangle

        size : tuple(int, int)
            The width and height of the rectangle
        """
        self.window = Window(background_colour, width, height)
        self.snake_size = (30, 30)
        self.snake = Snake((width//2, height//2), self.snake_size, (75, 75, 75))
        self.current_movement = Snake.move_up
        self.fruit_coordinates = (300, 210)
        self.fruit_size = (30, 30)
        self.running = True
        self.last_update_time = pygame.time.get_ticks()

    def handle_keydown(self, event):
        """Handle key input from the user.

        Check if the key pressed is any of the keys used to control the snake,
        that is any of the WASD-keys or the arrow keys, or ESC for quiting the game.

        If any of the WASD-keys or arrow keys are pressed, change direction of the snake
        to the appropiate direction.

        Parameters:
            event : pygame.event
                An event containing a pressed key.
        """

        pressed_key = event.key

        if pressed_key in (pygame.K_a, pygame.K_LEFT):
            self.current_movement = Snake.move_left
        elif pressed_key in (pygame.K_d, pygame.K_RIGHT):
            self.current_movement = Snake.move_right
        elif pressed_key in (pygame.K_w, pygame.K_UP):
            self.current_movement = Snake.move_up
        elif pressed_key in (pygame.K_s, pygame.K_DOWN):
            self.current_movement = Snake.move_down
        elif pressed_key == pygame.K_ESCAPE:
            self.running = False

    def draw(self):
        """Makes sure all the components of the game are presented on the screen."""
        self.window.draw_rect(
            (255, 0, 0),
            self.fruit_coordinates,
            self.fruit_size
        )

        for part in self.snake:
            coordinates = part.get_coordinates()
            size = part.get_size()
            colour = part.get_colour()
            self.window.draw_rect(
                colour,
                coordinates,
                size
            )

    def move_fruit(self):
        """
        Randomly moves the fruit until it does not collide with the snake anymore.
        Used after the fruit is picked up.
        """
        while True:
            screen_size = (self.window.width(), self.window.height()) # 600 , 600
            new_x = randrange(0, screen_size[0] - self.fruit_size[0], self.fruit_size[0]) # randrange(0, 570, 30)
            new_y = randrange(0, screen_size[1] - self.fruit_size[1], self.fruit_size[1]) # randrange(0, 570, 30)
            self.fruit_coordinates = (new_x, new_y)

            position_ok = True

            if self.snake.check_collision(self.fruit_coordinates, self.fruit_size):
                position_ok = False

            if position_ok:
                break

    def fruit_pickup(self):
        """
        Used to control if the snake is able to pick up the fruit.
        If the snake is able to pick the fruit up, the snake will grow
        and the fruit will be moved to a new position.
        """
        if self.snake.check_collision_with_fruit(self.fruit_coordinates, self.fruit_size):
            self.move_fruit()
            self.snake.grow()

    def is_inside_window(self):
        """
        Used to control whether the snake is inside the boundaries of
        the screen or not. If the snake is not inside the boundaries,
        the game is over.

        Return: bool
            True: Inside window
            False: Not inside window
        """
        screen_size = (self.window.width(), self.window.height())
        
        if self.snake.inside_bounds(
                (0, 0),
                (screen_size[0] - self.snake_size[0],
                 screen_size[1] - self.snake_size[1])):

            return True
        return False

    def update_move(self):
        """
        Function to update the movement and control if the
        snake collides with itself.

        Called through a pygame registered event.
        """
        self.current_movement(self.snake)
        if self.snake.check_collision_with_self() or not self.is_inside_window():
            self.running = False

    def run_game_logic(self):
        """
        The entry point of the game.
        Clears the screen, runs the game logic, and make sure that the
        screen is presented at the end.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event)

        time_since_update = pygame.time.get_ticks() - self.last_update_time

        if time_since_update > 150:
            self.last_update_time = pygame.time.get_ticks()
            self.update_move()

        self.fruit_pickup()

        self.draw()

    def game_loop(self):
        """
        The main loop of the game.

        Will continue to play until running is set to false.
        """
        self.running = True
        while self.running:
            self.window.clear()
            self.run_game_logic()
            pygame.display.flip()
