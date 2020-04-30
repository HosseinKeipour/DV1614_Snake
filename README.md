# DV1614_Snake

Assignment 2: Snake!
(Not to be confused with python, another kind of snake)
Scope: 1.5hp

Subjects to Cover: Basic object oriented programming. Iterators.

Estimated preparation time: 10 hours

Estimated time for exercises: 15 hours

Estimated implementation time: 15 hours

Description
Snake is a classic game dating back to 1976. It has since been remade hundreds of times with the most famous probably being the versions featured in the Nokia mobile phones since -98. 

The player starts as a small snake, often no more than a block, and the goal is to eat in order to grow. For each fruit eaten the snake controlled by the player grows by one block. If the player should steer the snake into itself or into a wall the game is over. Different Snake versions count the score differently.

 

Implementation Details
Together with this assignment, you are given a script containing the game-logic for the game Snake. You are to implement the Snake-class that is used in the game. As such, certain requirements are placed not only on the API of the Snake-class but also the internal structure. Make sure you have read and understood these details before you begin coding. All form of collision is to be solved with a rectangle against rectangle check.

All your code is to be placed in the folder "student_code".

Snake
File: snake_class.py

Snake is the main class that is to be implemented for this assignment. The following API must be followed:

A constructor (__init__) function taking the following arguments:
Starting position of the head (tuple with x- and y-values)
Coordinates for the top-left part of the block representing the head of the snake.
Size of the blocks that are to build up the snake (tuple with width and height)
Colour of the blocks that are to build up the snake (tuple with colour values (r,g,b))
move_left, move_right, move_up, and move_down (movement functions):
Moves the head one block-length in the desired direction
The rest of the body must follow the head, but cannot always be directly moved in the desired direction
inside_bounds:
Takes two arguments (tuple, tuple):
The first tuple is the top left coordinates of the bound
The second tuple is the bottom right coordinates of the bound
Both of these are ordered (x, y)
Returns bool:
True if the snake is completely inside the given bounds
Note: The snake is inside the given bounds if the right side of the snake coincide with the right side of the given bounds.
False otherwise
check_collision:
Takes two arguments (tuple, tuple):
The first tuple is the top left coordinates of the shape to check collision with
The second tuple is the width and height of the shape to check collision with
Returns bool:
True if any of the body-parts of the snake collide
False otherwise
check_collision_with_fruit
Takes two arguments (tuple, tuple):
The first tuple is the top left coordinates of the shape to check collision with
The second tuple is the width and height of the shape to check collision with
Returns bool:
True if the head of the snake completely overlaps with the fruit
False otherwise
check_collision_with_self
Returns bool:
True if the snake collide with itself
False otherwise
grow:
Add another body part to the snake
The blocks building up the snake must be created in a separate class with the following methods:

get_coordinates()
Return the x- and y-coordinates as a tuple
get_size()
Return the width and height as a tuple
get_colour()
Return the colour of the block as a tuple (r, g, b)
These blocks must be reachable from outside the snake through an iterator. That is, the class Snake must be iterable and usable according to the following code:

snake = Snake((0,0), (30, 30), (255, 0, 150))

for part in snake:
 
Other requirements:
Your file containing the implementation of the class Snake must be named snake_class.py.

You are allowed to put helper structures in other files.

Your code must pass the enclosed tests to be assessed.

Your code is to be placed in the folder "student_code".

Your code must reach a linting value of at least 8/10 when the command pylint .\snake_class.py is executed.

You must write proper variable names.

You must write docstrings for the classes and methods and there within properly describe usage, arguments and returns.

 

Testing your submission:
Provided with the files below is a test suite designed to test your code as your write it. Simply run this file as you would a normal Python file.

The file to execute to run the tests is run_tests.py.

The file to execute to run the game is snake_main.py.

It is recommended to continuously run the tests during development of your solution.
