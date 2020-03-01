"""
This module contains the Snake class and Build class, the former contains
    moving functions,
    inside bounds check function,
    collision check functions and
    grow function for the Snake class.

    The latter contains getter functions and setter functions.
"""

class Snake:
    """
    A structure for a Snake game.

    Attributes:
    -----------------
        head_position : list(int, int)
            Starting position of the head.
            Coordinates for the top-left part of the block representing the head of the snake.

        size : tuple(int, int)
            Size of the blocks that are to build up the snake.

        colour : tuple(r, g, b)
            Colour of the blocks that are to build up the snake.

        snake_head :
            The controllable head of snake that is build in a seperate class named Build.

        snake_body :
            A list which keeps each part of snake bodies from head to tail.

        snake_body.append(self.snake_head) :
            append the first part of snake body base on initial values

        _index :
            An index for itter function.

    Methods:
    -----------------
        move_up()
            Function to change snake head position to the up.

        move_down()
            Function to change snake head position to the down.

        move_left()
            Function to change snake head position to the left.

        move_right()
            Function to change snake head position to the right.

        inside_bounds()
            Function to check head of snake be inside the prepared game window.

        check_collision()
            Function to check the fruit does not collide with the snake.

        check_collision_with_fruit()
            Function to check the head of snake collision with the fruit.

        check_collision_with_self()
            Function to check the head of snake does not collide with the other part of snake body.

        grow()
            Append new part to the last part of snake body.

        __iter__(), __len__(), __next__()
            Make Snake class iterable.
    """
    def __init__(self, start_position, snake_size, snake_colour):
        """
        Initialize the game. The parameters are passed on to the init function of Window

        Parameters:
        ------------------------------------------
            start_positon : tuple(int, int)
                The x- and y-coordinates for Starting position of the head

            snake_size : tuple(int, int)
                The width and height of the blocks that are to build up the snake

            snake_colour : list(int, int, int)
                A triple of values (r, g, b) between 0 and 255 indicating the snake colour
        """
        self.head_position = list(start_position)
        self.size = snake_size
        self.colour = snake_colour
        self.snake_head = Build(self.head_position, self.size, self.colour)
        self.snake_body = []
        self.snake_body.append(self.snake_head)
        self._index = 0

    def move_up(self):
        """
        Moves the head one block-length in the up direction.

        Then the rest of the body follow the head.
        """

        old_head_position = self.snake_body[0].get_coordinates()
        self.head_position[1] = self.head_position[1] - self.size[1]

        if len(self.snake_body) > 1:
            for i in range(1, len(self.snake_body)):
                if len(self.snake_body)-i != 1:
                    body_position = self.snake_body[len(self.snake_body)-i-1].get_coordinates()
                    self.snake_body[len(self.snake_body)-i].set_coordinates(
                        [body_position[0], body_position[1]]
                    )
                else:
                    self.snake_body[1].set_coordinates([old_head_position[0], old_head_position[1]])

    def move_down(self):
        """
        Moves the head one block-length in the down direction.

        Then the rest of the body follow the head.
        """
        old_head_position = self.snake_body[0].get_coordinates()
        self.head_position[1] = self.head_position[1] + self.size[1]

        if len(self.snake_body) > 1:
            for i in range(1, len(self.snake_body)):
                if len(self.snake_body)-i != 1:
                    body_position = self.snake_body[len(self.snake_body)-i-1].get_coordinates()
                    self.snake_body[len(self.snake_body)-i].set_coordinates(
                        [body_position[0], body_position[1]]
                    )
                else:
                    self.snake_body[1].set_coordinates([old_head_position[0], old_head_position[1]])

    def move_left(self):
        """
        Moves the head one block-length in the left direction.

        Then the rest of the body follow the head.
        """
        old_head_position = self.snake_body[0].get_coordinates()
        self.head_position[0] = self.head_position[0] - self.size[0]

        if len(self.snake_body) > 1:
            for i in range(1, len(self.snake_body)):
                if len(self.snake_body)-i != 1:
                    body_position = self.snake_body[len(self.snake_body)-i-1].get_coordinates()
                    self.snake_body[len(self.snake_body)-i].set_coordinates(
                        [body_position[0], body_position[1]]
                    )
                else:
                    self.snake_body[1].set_coordinates([old_head_position[0], old_head_position[1]])

    def move_right(self):
        """
        Moves the head one block-length in the right direction.

        Then the rest of the body follow the head.
        """
        old_head_position = self.snake_body[0].get_coordinates()
        self.head_position[0] = self.head_position[0] + self.size[0]

        if len(self.snake_body) > 1:
            for i in range(1, len(self.snake_body)):
                if len(self.snake_body)-i != 1:
                    body_position = self.snake_body[len(self.snake_body)-i-1].get_coordinates()
                    self.snake_body[len(self.snake_body)-i].set_coordinates(
                        [body_position[0], body_position[1]]
                    )
                else:
                    self.snake_body[1].set_coordinates([old_head_position[0], old_head_position[1]])

    def inside_bounds(self, top_left, bottom_right):
        '''
        Used to control whether the snake is inside the boundaries of
        the screen or not. If the snake is not inside the boundaries,
        the game is over.

        Parameters:
            top_left : tuple(int, int)
                The top left coordinates of the bound.

            bottom_right : tuple(int, int)
                the bottom right coordinates of the bound.

        Return: bool
            True: Snake is completely inside the given bounds
            False: Otherwise
        '''
        if (top_left[0] <= self.head_position[0] and
                self.head_position[0] <= bottom_right[0]
           ):
            if (top_left[1] <= self.head_position[1] and
                    self.head_position[1] <= bottom_right[1]
               ):
                if (self.head_position[0] + self.size[0] <= bottom_right[0] - top_left[0] and
                        self.head_position[1] + self.size[1] <= bottom_right[1] - top_left[1]
                   ):
                    return True
        return False

    def check_collision(self, fruit_coordinates, fruit_size):
        """
        Function to check the fruit does not collide with the snake.

        Parameters:
            fruit_coordinates : tuple(int, int)
                A tuple of the top left coordinates of the new fruit to check collision with.
                New fruit coordinates is generated in move_fruit function in snake_game module.

            fruit_size : tuple(int, int)
                A tuple of the width and height of the new fruit to check collision with.

        Return: bool
            True:  If any of the body-parts of the snake collide
            False: Otherwise
        """
        for part in self.snake_body:
            if fruit_coordinates == part.get_coordinates():
                return True
        return False

    def check_collision_with_fruit(self, fruit_coordinates, fruit_size):
        """
        Function to check the snake collision with the fruit.

        Parameters:
            fruit_coordinates : tuple(int, int)
                The top left coordinates of the fruit to check collision with.

            fruit_size : tuple(int, int)
                The width and height of the fruit to check collision with.

        Return: bool
            True: If the head of the snake completely overlaps with the fruit
            False: Otherwise
        """
        if (fruit_coordinates[0] == self.head_position[0] and
                fruit_coordinates[1] == self.head_position[1]
           ):
            return True
        return False

    def check_collision_with_self(self):
        """
        Function to check the snake head collision with other part of the body.

        For snake with size only one block the test return False.

        Return: bool
            True: If the snake collide with itself
            False: Otherwise
        """
        if len(self.snake_body) > 1:
            for i in range(1, len(self.snake_body)):
                if self.snake_body[0].coordinates == self.snake_body[i].coordinates:
                    return True
        return False

    def grow(self):
        """
        Used to add another body part to the snake body in two step.
        1. Create a new body part as same as the part of the snake body.
        2. Appned it to the snake body.
        """
        new_body_part = Build(
            self.snake_body[-1].coordinates,
            self.size,
            self.colour
        )
        self.snake_body.append(new_body_part)

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.snake_body)

    def __next__(self):
        if len(self) == self._index:
            self._index = 0
            raise StopIteration
        self._index += 1
        return self.snake_body[self._index-1]

class Build:
    """
    The blocks building up the snake are created here with the following attributes and methods.

    Attributes:
    -----------------
        coordinates : list(int, int)
            Coordinates for the top-left part of the snake body-part.

        size : tuple(int, int)
            Size of the blocks that are to build up the snake.

        colour : tuple(r, g, b)
            Colour of the blocks that are to build up the snake.

    Methods:
    -----------------
        get_coordinates()
            Return the x- and y-coordinates as a tuple.

        get_size()
            Return the width and height as a tuple.

        get_colour()
            Return the colour of the block as a tuple (r, g, b).

        set_coordinates()
            Function to set new value to snake body-part position.
    """
    def __init__(self, coordinates, size, colour):
        """
        Initialize the snake body-part.

        Parameters:
        ------------------------------------------
            coordinates : list(int, int)
                Coordinates for the top-left part of the snake body-part.

            size : tuple(int, int)
                Size of the blocks that are to build up the snake.

            colour : tuple(r, g, b)
                Colour of the blocks that are to build up the snake.
        """
        self.coordinates = coordinates
        self.size = size
        self.colour = colour

    def get_coordinates(self):
        """Return the x- and y-coordinates as a tuple."""
        return tuple(self.coordinates)

    def get_size(self):
        """Used to get size of snake body-part then return it."""
        return self.size

    def get_colour(self):
        """Return the colour of the block as a tuple (r, g, b)."""
        return self.colour

    def set_coordinates(self, new_coordinates):
        """Used to set new coordinates of snake body-part."""
        self.coordinates = new_coordinates
